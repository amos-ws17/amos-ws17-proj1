from __future__ import unicode_literals
from message_handler import MessageHandler

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


if __name__ == '__main__':
    arg_parser = create_argument_parser()
    args = arg_parser.parse_args()

    topics = parse_dialogue_argument(args.dialogues)

    handler = MessageHandler(topics)

    data = {}
    data['steps'] = []
    data['steps'].append(json.loads(handler.converse('What is Scrum about?', 'Session ID')))

    print json.dumps(data)
