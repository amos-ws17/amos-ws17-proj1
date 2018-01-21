from workstreambot.message_handler import MessageHandler

import json

def test_guide_endless():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_name'] == "action_explain"
    assert response['dialogue'][0]['response'].startswith('Scrum is an agile process that allows') #TODO Get value from dict
    assert response['dialogue'][1]['action_name'] == "action_continue"
    assert response['dialogue'][1]['response'].endswith('roles?') #TODO Get value from dict

    for x in range(1, 13):
        response = send_message(handler, "Yes", "test_session")
        assert response['sender'] == "test_session"
        assert len(response['dialogue']) == 2
        assert response['dialogue'][0]['action_name'] == "action_explain"
        #TODO Check response
        assert response['dialogue'][1]['action_name'] == "action_continue"
        #TODO Check response

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_name'] == "action_explain"
    assert response['dialogue'][0]['response'].startswith('Scrum is an agile process that allows') #TODO Get value from dict
    assert response['dialogue'][1]['action_name'] == "action_continue"
    assert response['dialogue'][1]['response'].endswith('roles?') #TODO Get value from dict


def test_guide_restart():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_name'] == "action_explain"
    assert response['dialogue'][0]['response'].startswith('Scrum is an agile process that allows') #TODO Get value from dict
    assert response['dialogue'][1]['action_name'] == "action_continue"
    assert response['dialogue'][1]['response'].endswith('roles?') #TODO Get value from dict

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_name'] == "action_explain"
    assert response['dialogue'][0]['response'].startswith('Product owner: ') #TODO Get value from dict
    assert response['dialogue'][1]['action_name'] == "action_continue"
    assert response['dialogue'][1]['response'].endswith('stories?') #TODO Get value from dict

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_name'] == "action_explain"
    assert response['dialogue'][0]['response'].startswith('Scrum is an agile process that allows') #TODO Get value from dict
    assert response['dialogue'][1]['action_name'] == "action_continue"
    assert response['dialogue'][1]['response'].endswith('roles?') #TODO Get value from dict


def test_guide_reenter():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_name'] == "action_explain"
    assert response['dialogue'][0]['response'].startswith('Scrum is an agile process that allows') #TODO Get value from dict
    assert response['dialogue'][1]['action_name'] == "action_continue"
    assert response['dialogue'][1]['response'].endswith('roles?') #TODO Get value from dict

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_name'] == "action_explain"
    assert response['dialogue'][0]['response'].startswith('Product owner: ') #TODO Get value from dict
    assert response['dialogue'][1]['action_name'] == "action_continue"
    assert response['dialogue'][1]['response'].endswith('stories?') #TODO Get value from dict

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0


def send_message(handler, message, session_id):
    return json.loads(handler.converse(unicode(message), session_id))