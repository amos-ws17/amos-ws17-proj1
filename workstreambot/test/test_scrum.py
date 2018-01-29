import json

import workstreambot.scrum.dictionary as dict
from workstreambot.message_handler import MessageHandler


def test_guide_endless():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is Scrum about?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    theme = get_first_theme()
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.scrum[theme]['general']
    assert response['dialogue'][1]['action_type'] == "continue"
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}, {"text": "no", "reply": "no"}]

    for i in range(0, len(dict.scrum) - 2):
        response = send_message(handler, "Yes", "test_session")
        assert response['sender'] == "test_session"
        assert len(response['dialogue']) == 2
        assert response['dialogue'][0]['action_type'] == "explain"
        assert response['dialogue'][0]['title'] == theme
        assert response['dialogue'][0]['content'] == dict.scrum[theme]['general']
        assert response['dialogue'][1]['action_type'] == "continue"
        # TODO Check content
        assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"},
                                                           {"text": "no", "reply": "no"}]
        theme = get_next_theme(theme)

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.scrum[theme]['general']
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['content'] == 'That is it for the crash course in scrum. Would you like to restart?'
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}, {"text": "no", "reply": "no"}]


def test_guide_restart():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is Scrum about?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    theme = get_first_theme()
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.scrum[theme]['general']
    assert response['dialogue'][1]['action_type'] == "continue"
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}, {"text": "no", "reply": "no"}]

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.scrum[theme]['general']
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}, {"text": "no", "reply": "no"}]

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "What is Scrum about?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    theme = get_first_theme()
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.scrum[theme]['general']
    assert response['dialogue'][1]['action_type'] == "continue"
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}, {"text": "no", "reply": "no"}]


def test_guide_reenter():
    handler = MessageHandler({"scrum"})
    response = send_message(handler, "What is Scrum about?", "test_session")
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


def get_first_theme():
    for theme in dict.scrum:
        if dict.scrum[theme]['position'] == 1:
            return theme


def get_next_theme(current_theme):
    for theme in dict.scrum:
        if dict.scrum[theme]['position'] == dict.scrum[current_theme]['position'] + 1:
            return theme
    return None
