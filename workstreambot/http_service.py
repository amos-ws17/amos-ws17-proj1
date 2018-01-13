from flask import Flask, request
from message_handler import MessageHandler

import argparse

app = Flask(__name__)
handler = None

def create_argument_parser():
    parser = argparse.ArgumentParser(
        description='starts the bot')
    parser.add_argument(
        '-d', '--dialogues',
        required=True,
        type=str,
        help='dialogues to load')

    return parser

@app.route("/service/converse/<session_id>", methods=['GET', 'POST'])
def converse(session_id):
    query = request.args.get('query')

    if handler is None:
        return 'Services is not started.'

    response = handler.converse(query, session_id)
    return response, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    arg_parser = create_argument_parser()
    args = arg_parser.parse_args()

    topics = args.dialogues.split('+')

    handler = MessageHandler(topics)

    app.run(host='0.0.0.0', debug=False)
