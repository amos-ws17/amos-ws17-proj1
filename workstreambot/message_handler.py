from __future__ import unicode_literals
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter
from rasa_core.agent import Agent

import json


class MessageHandler:
    interpreter = None
    agents = None

    current_dialogue = None

    nlu_model_path = 'models/nlu/default/current'
    dialogue_path = '/models/dialogue'
    topic_switching_intent_prefix = 'switch_'

    def __init__(self, topics):
        self.interpreter = self.load_interpreter()
        self.agents = self.load_agents(topics)


    def load_interpreter(self):
        # where `model_directory points to the folder the model is persisted in
        interpreter = Interpreter.load(self.nlu_model_path, RasaNLUConfig('nlu_model_config.json'))

        return interpreter


    def load_agents(self, topics):
        agents = {}

        for topic in topics:
            agent = Agent.load(topic + self.dialogue_path)
            agents[topic] = agent

        return agents


    def converse(self, message, session_id):
        # parse user input
        nlu_json_response = self.interpreter.parse(message)

        entities = []

        if len(nlu_json_response['entities']) > 0:

            for e in nlu_json_response['entities']:
                entity = e['entity'] + '=' + str(e['value'])
                entities.append(entity)

        global current_dialogue

        for topic in self.agents:
            topic_switching_intent = self.topic_switching_intent_prefix + topic

            if topic_switching_intent == nlu_json_response['intent']['name']:
                if self.current_dialogue != topic:
                    self.current_dialogue = topic
                    # TODO Restart current dialogue

        dialogue_message = '_' + nlu_json_response['intent']['name'] + '[' + ','.join(map(str, entities)) + ']'

        # handle user input
        dialogue = self.agents[self.current_dialogue].handle_message(dialogue_message)

        data = {}
        data['sender'] = session_id  # TODO Replace with session Id
        data['message'] = message
        data['dialogue_message'] = dialogue_message

        data['nlu'] = nlu_json_response

        data['dialogue'] = []
        for i in range(0, len(dialogue)):
            data['dialogue'].append(json.loads(dialogue[i]))

        return json.dumps(data)