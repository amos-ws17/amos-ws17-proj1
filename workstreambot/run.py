from __future__ import unicode_literals

import utils
import json

nlu_model_path = 'models/nlu/default/current'
dialogue_path = '/models/dialogue'

topic_switching_intent_prefix = 'inform_'

current_dialogue = None


def load_interpreter():
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Metadata, Interpreter

    # where `model_directory points to the folder the model is persisted in
    interpreter = Interpreter.load(nlu_model_path, RasaNLUConfig('nlu_model_config.json'))

    return interpreter


def load_agents(topics):
    from rasa_core.agent import Agent

    agents = {}

    for topic in topics:
        agent = Agent.load(topic + dialogue_path)
        agents[topic] = agent

    return agents


def run(interpreter, agents, message):
    # parse user input
    nlu_jsonResponse = interpreter.parse(message)

    entities = []

    if len(nlu_jsonResponse['entities']) > 0:

        for e in nlu_jsonResponse['entities']:
            entity = e['entity'] + '=' + e['value']
            entities.append(entity)

    global current_dialogue

    for topic in agents:
        topic_switching_intent = topic_switching_intent_prefix + topic

        if topic_switching_intent == nlu_jsonResponse['intent']['name']:
            if current_dialogue != topic:
                current_dialogue = topic
                #TODO Restart current dialogue

    # handle user input
    dialogue = agents[current_dialogue].handle_message(
        '_' + nlu_jsonResponse['intent']['name'] + '[' + ','.join(map(str, entities)) + ']')


    data = {}
    data['nlu'] = nlu_jsonResponse

    data['dialogue'] = []
    for i in range(0, len(dialogue)):
        data['dialogue'].append(json.loads(dialogue[i]))
    data['sender'] = 'Session ID' #TODO Replace with session Id
    data['message'] = message

    print json.dumps(data)


if __name__ == '__main__':
    arg_parser = utils.create_argument_parser()
    args = arg_parser.parse_args()

    interpreter = load_interpreter()
    topics = utils.parse_dialogue_argument(args.dialogues)
    agents = load_agents(topics)

    run(interpreter, agents, 'What is Scrum about?')