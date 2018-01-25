import json

import workstreambot.scrum.dictionary as Dict
from workstreambot.message_handler import MessageHandler


def test_guide_endless():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['title'] == Dict.scrum_general_keys[0]
    assert response['dialogue'][0]['content'] == Dict.scrum_general_keys_values[Dict.scrum_general_keys[0]]
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['content'].endswith(Dict.scrum_general_keys[1] + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]

    for i in range(1, 12):
        response = send_message(handler, "Yes", "test_session")
        assert response['sender'] == "test_session"
        assert len(response['dialogue']) == 2
        assert response['dialogue'][0]['action_type'] == "explain"
        assert response['dialogue'][0]['title'] == Dict.scrum_general_keys[i]
        assert response['dialogue'][0]['content'] == Dict.scrum_general_keys_values[Dict.scrum_general_keys[i]]
        assert response['dialogue'][1]['action_type'] == "continue"
        # TODO Check content
        assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['title'] == Dict.scrum_general_keys[12]
    assert response['dialogue'][0]['content'] == Dict.scrum_general_keys_values[Dict.scrum_general_keys[12]]
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['content'] == 'That is it for the crash course in scrum. Would you like to restart?'
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]


def test_guide_restart():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['title'] == Dict.scrum_general_keys[0]
    assert response['dialogue'][0]['content'] == Dict.scrum_general_keys_values[Dict.scrum_general_keys[0]]
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['content'].endswith(Dict.scrum_general_keys[1] + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['title'] == Dict.scrum_general_keys[1]
    assert response['dialogue'][0]['content'] == Dict.scrum_general_keys_values[Dict.scrum_general_keys[1]]
    assert response['dialogue'][1]['content'].endswith(Dict.scrum_general_keys[2] + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['title'] == Dict.scrum_general_keys[0]
    assert response['dialogue'][0]['content'] == Dict.scrum_general_keys_values[Dict.scrum_general_keys[0]]
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['content'].endswith(Dict.scrum_general_keys[1] + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]


def test_guide_reenter():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][1]['action_type'] == "continue"

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][1]['action_type'] == "continue"

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "Yes", "test_session")  # TODO This input will mess up the dialogue
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0


def send_message(handler, message, session_id):
    return json.loads(handler.converse(message, session_id))
