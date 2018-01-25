import json

from workstreambot.message_handler import MessageHandler


def test_switch_scrum_intent():
    assert perform_initial_input("What is Scrum about?") == "switch_scrum"
    assert perform_initial_input("What's Scrum about?") == "switch_scrum"
    assert perform_initial_input("What about Scrum?") == "switch_scrum"
    # TODO Add to training data: assert perform_initial_input("Tell me more about Scrum") == "switch_scrum"
    # TODO Add to training data: assert perform_initial_input("Tell me something about Scrum") == "switch_scrum"
    # TODO Add to training data: assert perform_initial_input("How is this in Scrum?") == "switch_scrum"


def test_continue_intent():
    assert perform_single_continue("Yes") == "continue"
    # TODO Add to training data: assert perform_single_continue("What is about Scrum?", "Continue") == "affirm"
    assert perform_single_continue("Ok") == "continue"
    assert perform_single_continue("Please yes") == "continue"
    assert perform_single_continue("Yes please") == "continue"


def test_denys_intent():
    assert perform_single_continue("No") == "deny"
    # TODO Add to training data: assert perform_single_continue("Don't continue") == "deny"
    # TODO Add to training data: assert perform_single_continue("Stop") == "deny"
    assert perform_single_continue("No thanks") == "deny"


def perform_initial_input(initial_input):
    handler = MessageHandler({"scrum"})
    response = send_message(handler, initial_input, "test_session")
    return response['nlu']['intent']['name']


def perform_single_continue(continue_input):
    handler = MessageHandler({"scrum"})
    send_message(handler, "What is about Scrum?", "test_session")

    response = send_message(handler, continue_input, "test_session")
    return response['nlu']['intent']['name']


def send_message(handler, message, session_id):
    return json.loads(handler.converse(message, session_id))
