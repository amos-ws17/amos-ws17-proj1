from __future__ import unicode_literals

import argparse

nlu_training_data_path = 'data/'
domain_file_path = '/domain.yml'
dialogue_model_path = '/models/dialogue'
stories_file_path = '/data/stories.md'
separator = '+'

def create_argument_parser():
    parser = argparse.ArgumentParser(
        description='starts the bot')
    parser.add_argument(
        '-d', '--dialogues',
        required=True,
        type=str,
        help='dialogues to load')
    parser.add_argument(
        '-n', '--nlu_data',
        required=True,
        type=str,
        help='nlu training data file')

    return parser


def parse_dialogue_argument(argument):
    return argument.split(separator)


def train_nlu(nlu_training_data):
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.converters import load_data
    from rasa_nlu.model import Trainer

    training_data = load_data(nlu_training_data_path + nlu_training_data)
    trainer = Trainer(RasaNLUConfig('nlu_model_config.json'))
    trainer.train(training_data)
    trainer.persist('models/nlu/', fixed_model_name='current')


def train_dialogue(topic):
    from rasa_core.agent import Agent
    from rasa_core.policies.keras_policy import KerasPolicy
    from rasa_core.policies.memoization import MemoizationPolicy

    domain_file = topic + domain_file_path
    model_path = topic + dialogue_model_path
    stories_file = topic + stories_file_path

    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy()])
    agent.train(stories_file)
    agent.persist(model_path)


def train_models(topics, nlu_training_data):
    # train nlu
    train_nlu(nlu_training_data)
    # train dialogue
    for topic in topics:
        train_dialogue(topic)


if __name__ == '__main__':
    arg_parser = create_argument_parser()
    args = arg_parser.parse_args()
    nlu_training_data = args.nlu_data
    topics = parse_dialogue_argument(args.dialogues)

    train_models(topics, nlu_training_data)
