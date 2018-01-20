from workstreambot.message_handler import MessageHandler

import json

handler = MessageHandler({"scrum"})

def test_function():
    response = send_message("What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert response['dialogue'][0]['action_name'] == "action_explain"
    assert response['dialogue'][1]['action_name'] == "action_continue"


def send_message(message, session_id):
    return json.loads(handler.converse(unicode(message), session_id))