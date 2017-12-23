from __future__ import unicode_literals

import argparse
import json

nlu_model_path = 'models/nlu/default/current'
dialogue_path = '/models/dialogue'
separator = '+'
topic_switching_intent_prefix = 'switch_'

current_dialogue = None


def create_argument_parser():
    parser = argparse.ArgumentParser(
        description='starts the bot')
    parser.add_argument(
        '-d', '--dialogues',
        required=True,
        type=str,
        help='dialogues to load')

    return parser


def parse_dialogue_argument(argument):
    return argument.split(separator)


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
    nlu_json_response = interpreter.parse(message)

    entities = []

    if len(nlu_json_response['entities']) > 0:

        for e in nlu_json_response['entities']:
            entity = e['entity'] + '=' + str(e['value'])
            entities.append(entity)

    global current_dialogue

    for topic in agents:
        topic_switching_intent = topic_switching_intent_prefix + topic

        if topic_switching_intent == nlu_json_response['intent']['name']:
            if current_dialogue != topic:
                current_dialogue = topic
                # TODO Restart current dialogue

    dialogue_message = '_' + nlu_json_response['intent']['name'] + '[' + ','.join(map(str, entities)) + ']'

    # handle user input
    dialogue = agents[current_dialogue].handle_message(dialogue_message)

    data = {}
    data['sender'] = 'Session ID'  # TODO Replace with session Id
    data['message'] = message
    data['dialogue_message'] = dialogue_message

    data['nlu'] = nlu_json_response

    data['dialogue'] = []
    for i in range(0, len(dialogue)):
        data['dialogue'].append(json.loads(dialogue[i]))

    return json.dumps(data)


if __name__ == '__main__':
    arg_parser = create_argument_parser()
    args = arg_parser.parse_args()

    interpreter = load_interpreter()
    topics = parse_dialogue_argument(args.dialogues)
    agents = load_agents(topics)

    data = {}
    data['steps'] = []
    data['steps'].append(json.loads(run(interpreter, agents, 'What is Scrum about?')))
    data['steps'].append(json.loads(run(interpreter, agents, 'What will the weather be in Berlin?')))
    data['steps'].append(json.loads(run(interpreter, agents, 'Yes')))

    print json.dumps(data)
