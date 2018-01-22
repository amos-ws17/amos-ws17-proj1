import json

from workstreambot.message_handler import MessageHandler


def test_guide_endless():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "action_explain"
    assert response['dialogue'][0]['title'] == "scrum"  # TODO Get value from dict
    assert response['dialogue'][0]['content'].startswith(
        'Scrum is an agile process that allows')  # TODO Get value from dict
    assert response['dialogue'][1]['action_type'] == "action_continue"
    assert response['dialogue'][1]['content'].endswith('roles?')  # TODO Get value from dict
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]  # TODO Get value from dict

    for x in range(1, 12):
        response = send_message(handler, "Yes", "test_session")
        assert response['sender'] == "test_session"
        assert len(response['dialogue']) == 2
        assert response['dialogue'][0]['action_type'] == "action_explain"
        # TODO Check title and content
        assert response['dialogue'][1]['action_type'] == "action_continue"
        # TODO Check content
        assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]  # TODO Get value from dict

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "action_explain"
    assert response['dialogue'][0]['title'] == "goals"  # TODO Get value from dict
    assert response['dialogue'][0]['content'].startswith(
        'The goal of scrum is to ensure that the development of the product')  # TODO Get value from dict
    assert response['dialogue'][1]['action_type'] == "action_continue"
    assert response['dialogue'][1]['content'] == 'That is it for the crash course in scrum. Would you like to restart?'
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]  # TODO Get value from dict


def test_guide_restart():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "action_explain"
    assert response['dialogue'][0]['title'] == "scrum"  # TODO Get value from dict
    assert response['dialogue'][0]['content'].startswith(
        'Scrum is an agile process that allows')  # TODO Get value from dict
    assert response['dialogue'][1]['action_type'] == "action_continue"
    assert response['dialogue'][1]['content'].endswith('roles?')  # TODO Get value from dict
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]  # TODO Get value from dict

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "action_explain"
    assert response['dialogue'][0]['title'] == "roles"  # TODO Get value from dict
    assert response['dialogue'][0]['content'].startswith('Product owner: ')  # TODO Get value from dict
    assert response['dialogue'][1]['action_type'] == "action_continue"
    assert response['dialogue'][1]['content'].endswith('stories?')  # TODO Get value from dict
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]  # TODO Get value from dict

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "action_explain"
    assert response['dialogue'][0]['title'] == "scrum"  # TODO Get value from dict
    assert response['dialogue'][0]['content'].startswith(
        'Scrum is an agile process that allows')  # TODO Get value from dict
    assert response['dialogue'][1]['action_type'] == "action_continue"
    assert response['dialogue'][1]['content'].endswith('roles?')  # TODO Get value from dict
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]  # TODO Get value from dict


def test_guide_reenter():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is about Scrum?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "action_explain"
    assert response['dialogue'][0]['title'] == "scrum"  # TODO Get value from dict
    assert response['dialogue'][0]['content'].startswith(
        'Scrum is an agile process that allows')  # TODO Get value from dict
    assert response['dialogue'][1]['action_type'] == "action_continue"
    assert response['dialogue'][1]['content'].endswith('roles?')  # TODO Get value from dict
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]  # TODO Get value from dict

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "action_explain"
    assert response['dialogue'][0]['title'] == "roles"  # TODO Get value from dict
    assert response['dialogue'][0]['content'].startswith('Product owner: ')  # TODO Get value from dict
    assert response['dialogue'][1]['action_type'] == "action_continue"
    assert response['dialogue'][1]['content'].endswith('stories?')  # TODO Get value from dict
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes"}, {"text": "no"}]  # TODO Get value from dict

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0


def send_message(handler, message, session_id):
    return json.loads(handler.converse(message, session_id))
