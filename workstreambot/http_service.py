from flask import Flask, request
from message_handler import MessageHandler

app = Flask(__name__)
handler = None

@app.route("/service/setup", methods=['GET', 'POST'])
def setup_service():
    args = request.args.get('dia')

    if args is None:
        return 'Please define the dialogue topics to use per `dia` argument.'

    topics = args.split(' ')

    global handler

    handler = MessageHandler(topics)

    return "Service started with the following dialogue topics: " + ', '.join(map(str, topics))


@app.route("/service/converse/<session_id>", methods=['GET', 'POST'])
def converse(session_id):
    query = request.args.get('query')

    if handler is None:
        return 'Services is not started.'

    response = handler.converse(query, session_id)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
