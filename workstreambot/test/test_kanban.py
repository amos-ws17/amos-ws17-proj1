import json

import pytest

import workstreambot.kanban.dictionary as dict
from workstreambot.message_handler import MessageHandler


def test_guide_endless():
    handler = MessageHandler({"kanban"})
    response = send_message(handler, "What about Kanban?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    for i in range(0, len(dict.kanban) - 2):
        response = send_message(handler, "Yes", "test_session")
        assert response['sender'] == "test_session"
        assert len(response['dialogue']) == 2

        # Explain
        assert response['dialogue'][0]['action_type'] == "explain"
        assert response['dialogue'][0]['action_name'] == "explain"
        assert response['dialogue'][0]['title'] == theme
        assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
        if 'replyOptions' in response['dialogue'][0]:
            assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

        # Continue
        theme = get_next_theme(theme)
        assert response['dialogue'][1]['action_type'] == "continue"
        assert response['dialogue'][1]['action_name'] == "continue"
        assert response['dialogue'][1]['content'].endswith(theme + '?')
        assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

    # Continue
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'] == 'That is it for the crash course in kanban. Would you like to restart?'
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]


def test_guide_restart():
    handler = MessageHandler({"kanban"})
    response = send_message(handler, "What about Kanban?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "What about Kanban?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]


@pytest.mark.skip(reason="This test will fail, because the behavior is currently not supported")
def test_guide_reenter():
    handler = MessageHandler({"kanban"})
    response = send_message(handler, "What about Kanban?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"

    response = send_message(handler, "No", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0

    response = send_message(handler, "Yes", "test_session")  # TODO This input will mess up the dialogue
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 0


def test_details():
    handler = MessageHandler({"kanban"})
    response = send_message(handler, "What about Kanban?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    detail = "history"
    response = send_message(handler, "Tell me more about " + detail, "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain Detail
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain_detail"
    assert response['dialogue'][0]['title'] == detail
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['details'][detail]
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], filter_details(theme, detail))

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]


def test_continue_details():
    handler = MessageHandler({"kanban"})
    response = send_message(handler, "What about Kanban?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    detail = "history"
    response = send_message(handler, "Tell me more about " + detail, "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain Detail
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain_detail"
    assert response['dialogue'][0]['title'] == detail
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['details'][detail]
    assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], filter_details(theme, detail))

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    detail = "kaizen"
    response = send_message(handler, "Tell me more about " + detail, "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain Detail
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain_detail"
    assert response['dialogue'][0]['title'] == detail
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['details'][detail]
    assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], filter_details(theme, detail))

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]


def test_continue_after_detail():
    handler = MessageHandler({"kanban"})
    response = send_message(handler, "What about Kanban?", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], dict.kanban[theme]['details'])

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    detail = "history"
    response = send_message(handler, "Tell me more about " + detail, "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain Detail
    theme = get_first_theme()
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain_detail"
    assert response['dialogue'][0]['title'] == detail
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['details'][detail]
    assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], filter_details(theme, detail))

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]

    response = send_message(handler, "Yes", "test_session")
    assert response['sender'] == "test_session"
    assert len(response['dialogue']) == 2

    # Explain
    assert response['dialogue'][0]['action_type'] == "explain"
    assert response['dialogue'][0]['action_name'] == "explain"
    assert response['dialogue'][0]['title'] == theme
    assert response['dialogue'][0]['content'] == dict.kanban[theme]['general']
    if 'replyOptions' in response['dialogue'][0]:
        assert reply_options_contain_details(response['dialogue'][0]['replyOptions'], filter_details(theme, detail))

    # Continue
    theme = get_next_theme(theme)
    assert response['dialogue'][1]['action_type'] == "continue"
    assert response['dialogue'][1]['action_name'] == "continue"
    assert response['dialogue'][1]['content'].endswith(theme + '?')
    assert response['dialogue'][1]['replyOptions'] == [{"text": "yes", "reply": "yes"}]


def send_message(handler, message, session_id):
    return json.loads(handler.converse(message, session_id))


def get_first_theme():
    for theme in dict.kanban:
        if dict.kanban[theme]['position'] == 1:
            return theme


def get_next_theme(current_theme):
    for theme in dict.kanban:
        if dict.kanban[theme]['position'] == dict.kanban[current_theme]['position'] + 1:
            return theme
    return None


def filter_details(current_theme, current_detail):
    details = []
    for detail in dict.kanban[current_theme]['details']:
        if detail != current_detail:
            details.append(detail)

    return details


def reply_options_contain_details(reply_options, details):
    for detail in details:
        detail_exists = False
        print(reply_options)
        for reply in reply_options:
            if reply['reply'] == "Tell me more about " + detail:
                detail_exists = True
        if not detail_exists:
            return False
    return True
