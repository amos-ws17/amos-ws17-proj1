import json


def getResponse(action_name, tracker, response):
    data = {}
    data['action_name'] = action_name
    data['paused'] = tracker.is_paused()
    data['slots'] = tracker.current_slot_values()
    data['response'] = response

    return json.dumps(data)
