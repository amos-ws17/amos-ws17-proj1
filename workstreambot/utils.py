import json


def prepare_action_response(action_name, title, content, reply_options, slots, topic):
    data = {}
    data['action_type'] = action_name
    data['content'] = content
    if title is not None:
        data['title'] = title
    if reply_options is not None and len(reply_options) > 0:
        data['replyOptions'] = reply_options
    if slots is not None and len(slots) > 0:
        data['slots'] = slots
    data['topic'] = topic

    return json.dumps(data)
