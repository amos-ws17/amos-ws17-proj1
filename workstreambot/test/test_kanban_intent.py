import json

import workstreambot.kanban.dictionary as dict
from workstreambot.message_handler import MessageHandler


def test_switch_kanban():
    nlu = perform_initial_input("What is Kanban about?")
    # TODO assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("What's Kanban about?")
    # TODO assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("What about Kanban?")
    assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("Tell me more about Kanban")
    # TODO assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("Tell me something about Kanban")
    # TODO assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("How is this in Kanban?")
    assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 0


def test_switch_kanban_theme():
    nlu = perform_initial_input("What are the meetings in Kanban?")
    assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 1
    assert entities_contain_theme(nlu['entities'])
    # TODO assert get_theme_value(nlu['entities']) == 'ceremonies'

    nlu = perform_initial_input("What are the ceremonies in Kanban?")
    assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 1
    assert entities_contain_theme(nlu['entities'])
    assert get_theme_value(nlu['entities']) == 'ceremonies'


def test_switch_kanban_detail():
    # TODO
    nlu = perform_initial_input("What is the history of Kanban?")
    assert nlu['intent']['name'] == "switch_kanban"
    assert len(nlu['entities']) == 1
    assert entities_contain_detail(nlu['entities'])
    assert get_detail_value(nlu['entities']) == 'history'


def test_inform_theme():
    # TODO
    nlu = perform_initial_input("What are the artefacts?")
    assert nlu['intent']['name'] == "inform"
    assert len(nlu['entities']) == 1
    assert entities_contain_theme(nlu['entities'])
    assert get_theme_value(nlu['entities']) == 'artefacts'


def test_inform_detail():
    # TODO
    nlu = perform_initial_input("What is the cycle time?")
    assert nlu['intent']['name'] == "inform"
    assert len(nlu['entities']) == 1
    assert entities_contain_detail(nlu['entities'])
    assert get_detail_value(nlu['entities']) == 'cycle time'


def test_details():
    for detail in get_all_details():
        nlu = perform_inform("Tell me more about " + detail)
        assert nlu['intent']['name'] == "inform", "Expected intent for " + detail + " is incorrect"
        assert len(nlu['entities']) == 1, "Expected entities for " + detail + " are incorrect"
        print(nlu['entities'])
        assert entities_contain_detail(nlu['entities']), "Expected entity for " + detail + " is incorrect"
        assert get_detail_value(nlu['entities']) == detail


def test_continue():
    assert perform_single_continue("Yes") == "continue"
    # TODO assert perform_single_continue("Continue") == "affirm"
    assert perform_single_continue("Ok") == "continue"
    assert perform_single_continue("Please yes") == "continue"
    assert perform_single_continue("Yes please") == "continue"


def test_denys():
    assert perform_single_continue("No") == "deny"
    # TODO assert perform_single_continue("Don't continue") == "deny"
    assert perform_single_continue("Stop") == "deny"
    assert perform_single_continue("No thanks") == "deny"


def perform_initial_input(initial_input):
    handler = MessageHandler({"kanban"})
    response = send_message(handler, initial_input, "test_session")
    return response['nlu']


def perform_single_continue(continue_input):
    handler = MessageHandler({"kanban"})
    send_message(handler, "What is Kanban about?", "test_session")

    response = send_message(handler, continue_input, "test_session")
    return response['nlu']['intent']['name']


def perform_inform(inform_input):
    handler = MessageHandler({"kanban"})
    send_message(handler, "What is Kanban about?", "test_session")

    response = send_message(handler, inform_input, "test_session")
    return response['nlu']


def send_message(handler, message, session_id):
    return json.loads(handler.converse(message, session_id))


def entities_contain_theme(entities):
    for entity in entities:
        if entity['entity'] == 'theme':
            return True
    return False


def get_theme_value(entities):
    for entity in entities:
        if entity['entity'] == 'theme':
            return entity['value']
    return None


def entities_contain_detail(entities):
    for entity in entities:
        if entity['entity'] == 'detail':
            return True
    return False


def get_detail_value(entities):
    for entity in entities:
        if entity['entity'] == 'detail':
            return entity['value']
    return None


def get_all_details():
    details = []
    for theme in dict.kanban:
        if 'details' in dict.kanban[theme]:
            for detail in dict.kanban[theme]['details']:
                details.append(detail)
    return details
