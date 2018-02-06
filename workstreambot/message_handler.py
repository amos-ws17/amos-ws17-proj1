from __future__ import unicode_literals

import json
import os

from rasa_core.agent import Agent
from rasa_core.domain import TemplateDomain
from rasa_core.tracker_store import *
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Interpreter
from session import Session


class MessageHandler:
    interpreter = None
    dialogue_models = {}

    sessions = {}

    nlu_model_path = 'models/nlu/default/current'
    dialogue_model_path = '/models/dialogue'
    switching_intent_prefix = 'switch_'
    domain_path="/domain.yml"

    def __init__(self, dialogue_topics, persistance=False):
        self.persistance = persistance
        self.interpreter = Interpreter.load(self.nlu_model_path, RasaNLUConfig('nlu_model_config.json'))
        self.dialogue_models = self.load_dialogue_models(dialogue_topics)

    def load_dialogue_models(self, dialogue_topics):
        dialogue_models = {}

        for dialogue_topic in dialogue_topics:
            dialogue_models[dialogue_topic] = self.load_dialogue_model(dialogue_topic)

        return dialogue_models

    def load_dialogue_model(self, topic):
        if self.persistance:
            # Load with persistance tracker
            domain = TemplateDomain.load(topic + self.domain_path)
            redis_tracker_store = RedisTrackerStoreAgentized(domain=domain, host="redis-container")
            redis_tracker_store.set_topic(topic)
            return Agent.load(topic + self.dialogue_model_path, tracker_store=redis_tracker_store)
        else:
            # Load with default tracker
            return Agent.load(topic + self.dialogue_model_path)

    def converse(self, message, session_id):
        # Parse user input
        nlu_json_response = self.interpreter.parse(message)
        entities = self.prepare_entities(nlu_json_response)

        # Select session
        if session_id not in self.sessions:
            self.sessions[session_id] = Session()

        current_dialogue_topic = self.sessions[session_id].get_current_dialogue_topic()

        # Select current dialogue topic
        for dialogue_topic in self.dialogue_models:
            switching_intent = self.switching_intent_prefix + dialogue_topic

            if switching_intent == nlu_json_response['intent']['name']:
                if current_dialogue_topic != dialogue_topic:
                    current_dialogue_topic = dialogue_topic
                    # Reset dialogue model
                    self.dialogue_models[current_dialogue_topic] = self.load_dialogue_model(current_dialogue_topic)
                    # TODO Inject slots
                    if current_dialogue_topic in self.sessions[session_id].all_topics:
                        #Ask user about restart or continue
                        dialogue_message = '_' + nlu_json_response['intent']['name'] + '[' + ','.join(map(str, entities)) + ']'
                        dialogue = self.dialogue_models[current_dialogue_topic].handle_message(text_message=dialogue_message,
                            sender_id=session_id)
                        dialogue = ['{"action_type":"", "content":"Would you like to restart or continue?", "title":"None", '
                                    '"replyOptions": [{"text": "restart", "reply": "restart"}, {"text": "continue", "reply": "continue"}]}']
                        # Save changes in session
                        self.sessions[session_id].set_current_dialogue_topic(current_dialogue_topic)
                        return self.prepare_response(session_id, message, dialogue_message, nlu_json_response, dialogue)
                    else:
                        self.sessions[session_id].add_new_topic(current_dialogue_topic)

        # Handle user input
        dialogue_message = '_' + nlu_json_response['intent']['name'] + '[' + ','.join(map(str, entities)) + ']'
        if current_dialogue_topic != None:
            if message == 'restart':
                dialogue_message = '_switch_' + current_dialogue_topic + '[]'
            dialogue = self.dialogue_models[current_dialogue_topic].handle_message(text_message=dialogue_message,
                                                                               sender_id=session_id)
            # Save changes in session
            self.sessions[session_id].set_current_dialogue_topic(current_dialogue_topic)
        else:
            dialogue = ['{"action_type":"", "content":"Sorry, I did not understand you!", "title":"None", "replyOptions": []}']

        return self.prepare_response(session_id, message, dialogue_message, nlu_json_response, dialogue)

    def prepare_entities(self, nlu_json_response):
        entities = []

        if len(nlu_json_response['entities']) > 0:

            for e in nlu_json_response['entities']:
                entity = e['entity'] + '=' + str(e['value'])
                entities.append(entity)

        return entities

    def prepare_response(self, session_id, message, dialogue_message, nlu_json_response, dialogue):
        data = {}
        data['sender'] = session_id
        data['message'] = message
        data['dialogue_message'] = dialogue_message

        data['nlu'] = nlu_json_response

        data['dialogue'] = []
        for i in range(0, len(dialogue)):
            data['dialogue'].append(json.loads(dialogue[i]))

        return json.dumps(data)


class RedisTrackerStoreAgentized(TrackerStore):

    def __init__(self, domain, mock=False, host='192.168.99.100',
                 port=6379, db=0, password=None):

        if mock:
            import fakeredis
            self.red = fakeredis.FakeStrictRedis()
        else:  # pragma: no cover
            import redis
            self.red = redis.StrictRedis(host=host, port=port, db=db,
                                         password=password)
        super(RedisTrackerStoreAgentized, self).__init__(domain)
        self.topic = ""

    def set_topic(self, topic):
        self.topic = topic

    def save(self, tracker, timeout=None):
        serialised_tracker = RedisTrackerStore.serialise_tracker(tracker)
        self.red.set(self.topic + "_" + tracker.sender_id, serialised_tracker, ex=timeout)

    def retrieve(self, sender_id):
        key = self.topic + "_" + sender_id
        stored = self.red.get(key)
        if stored is not None:
            return self.deserialise_tracker(key, stored)
        else:
            return None

    def clean(self):
        for key in self.red.scan_iter(self.topic + "*"):
            self.red.delete(key)