from __future__ import unicode_literals
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter
from rasa_core.agent import Agent
from session import Session

import json


class MessageHandler:
    interpreter = None
    dialogue_topics = None
    dialogue_models = {}

    sessions = {}

    nlu_model_path = 'models/nlu/default/current'
    dialogue_model_path = '/models/dialogue'
    switching_intent_prefix = 'switch_'

    def __init__(self, dialogue_topics):
        self.interpreter = Interpreter.load(self.nlu_model_path, RasaNLUConfig('nlu_model_config.json'))
        self.dialogue_topics = dialogue_topics
        self.dialogue_models = self.load_dialogue_models(dialogue_topics)

    def load_dialogue_models(self, dialogue_topics):
        dialogue_models = {}

        for dialogue_topic in dialogue_topics:
            dialogue_models[dialogue_topic] = self.load_dialogue_model(dialogue_topic)

        return dialogue_models

    def load_dialogue_model(self, topic):
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

        # Handle user input
        dialogue_message = '_' + nlu_json_response['intent']['name'] + '[' + ','.join(map(str, entities)) + ']'
        dialogue = self.dialogue_models[current_dialogue_topic].handle_message(text_message=dialogue_message, sender_id=session_id)

        # Save changes in session
        self.sessions[session_id].set_current_dialogue_topic(current_dialogue_topic)

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
