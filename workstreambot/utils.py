import json


def prepare_action_response(action_type, content, action_name=None, title=None, reply_options=None, slots=None,
                            topic=None):
    data = dict()
    data['action_type'] = action_type
    data['content'] = content
    if action_name is not None:
        data['action_name'] = action_name
    if title is not None:
        data['title'] = title
    if reply_options is not None and len(reply_options) > 0:
        data['replyOptions'] = reply_options
    if slots is not None and len(slots) > 0:
        data['slots'] = slots
    if topic is not None:
        data['topic'] = topic

    return json.dumps(data)
