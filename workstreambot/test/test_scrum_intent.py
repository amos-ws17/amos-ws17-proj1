import json

import workstreambot.scrum.dictionary as dict
from workstreambot.message_handler import MessageHandler


def test_switch_scrum():
    nlu = perform_initial_input("What is Scrum about?")
    assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("What's Scrum about?")
    assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("What about Scrum?")
    assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("Tell me more about Scrum")
    # TODO assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("Tell me something about Scrum")
    # TODO assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 0

    nlu = perform_initial_input("How is this in Scrum?")
    # TODO assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 0


def test_switch_scrum_theme():
    nlu = perform_initial_input("What are the roles in Scrum?")
    assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 1
    assert entities_contain_theme(nlu['entities'])
    assert get_theme_value(nlu['entities']) == 'roles'

    nlu = perform_initial_input("What are the meetings in Scrum?")
    assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 1
    assert entities_contain_theme(nlu['entities'])
    # TODO assert theme_value_is_equal(nlu['entities'], 'ceremonies'), "Theme value is " + nlu['entities'][0]['value'] + ", instead of ceremonies"

    nlu = perform_initial_input("What are the ceremonies in Scrum?")
    # TODO assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 1
    assert entities_contain_theme(nlu['entities'])
    assert get_theme_value(nlu['entities']) == 'ceremonies'


def test_switch_scrum_detail():
    # TODO
    nlu = perform_initial_input("What is the role of the developers in scrum?")
    assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 1
    assert entities_contain_detail(nlu['entities'])
    assert get_detail_value(nlu['entities']) == 'developers'

    nlu = perform_initial_input("What does the Product Owner in Scrum?")
    # TODO assert nlu['intent']['name'] == "switch_scrum"
    assert len(nlu['entities']) == 1
    assert entities_contain_detail(nlu['entities'])
    assert get_detail_value(nlu['entities']) == 'Product Owner'


def test_inform_theme():
    # TODO
    nlu = perform_initial_input("Tell me about the roles")
    assert nlu['intent']['name'] == "inform"
    assert len(nlu['entities']) == 1
    assert entities_contain_theme(nlu['entities'])
    assert get_theme_value(nlu['entities']) == 'roles'


def test_inform_detail():
    # TODO
    nlu = perform_initial_input("Tell me more about the Product Owner")
    assert nlu['intent']['name'] == "inform"
    assert len(nlu['entities']) == 1
    assert entities_contain_detail(nlu['entities'])
    assert get_detail_value(nlu['entities']) == 'Product Owner'


def test_details():
    for detail in get_all_details():
        nlu = perform_inform("Tell me more about " + detail)
        assert nlu['intent']['name'] == "inform", "Expected intent for " + detail + " is incorrect"
        assert len(nlu['entities']) == 1, "Expected entities for " + detail + " are incorrect"
        assert entities_contain_detail(nlu['entities']), "Expected entity for " + detail + " is incorrect"
        assert get_detail_value(nlu['entities']) == detail


def test_continue():
    assert perform_single_continue("Yes") == "continue"
    # TODO Add to training data: assert perform_single_continue("What is about Scrum?", "Continue") == "affirm"
    assert perform_single_continue("Ok") == "continue"
    assert perform_single_continue("Please yes") == "continue"
    assert perform_single_continue("Yes please") == "continue"


def test_denys():
    assert perform_single_continue("No") == "deny"
    # TODO Add to training data: assert perform_single_continue("Don't continue") == "deny"
    # TODO Add to training data: assert perform_single_continue("Stop") == "deny"
    assert perform_single_continue("No thanks") == "deny"


def perform_initial_input(initial_input):
    handler = MessageHandler({"scrum"})
    response = send_message(handler, initial_input, "test_session")
    return response['nlu']


def perform_single_continue(continue_input):
    handler = MessageHandler({"scrum"})
    send_message(handler, "What is Scrum about?", "test_session")

    response = send_message(handler, continue_input, "test_session")
    return response['nlu']['intent']['name']


def perform_inform(inform_input):
    handler = MessageHandler({"scrum"})
    send_message(handler, "What is Scrum about?", "test_session")

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
    for theme in dict.scrum:
        if 'details' in dict.scrum[theme]:
            for detail in dict.scrum[theme]['details']:
                details.append(detail)
    return details
