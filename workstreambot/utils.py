import argparse

separator = '+'


def create_argument_parser():
    """Parse all the command line arguments for the run script."""

    parser = argparse.ArgumentParser(
        description='starts the bot')
    parser.add_argument(
        '-d', '--dialogues',
        required=True,
        type=str,
        help="dialogues to load")

    return parser


def parse_dialogue_argument(argument):
    return argument.split(separator)
