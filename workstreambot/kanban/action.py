from rasa_core.actions import Action
import kanban.dictionary as dict
import utils as utils

sessions = {}

# get the next key to explain
def get_next_kanban_key(index):
    try:
        key = dict.kanban_general_keys[index]
        return key
    except IndexError:
        return None

# get the index of the details being explained
def find_kanban_detail_index(key):
    keys = dict.kanban_details_keys
    for i in range(len(keys)):
        if key in keys[i]:
            return i
    return None


# get the index of the theme being explained
def find_kanban_general_index(key):
    keys = dict.kanban_general_keys
    for i in range(len(keys)):
        if key in keys[i]:
            return i
    return None


# find a specific key to explain
# def find_kanban_key(key):
#     if key in K.kanbanGeneralKeysValues:
#         return key
#     else if key in K.kanbanDetailsKeysValues:
#         return key
#     else:
#         return None

def entities_contain_detail(entities):
    if len(entities) == 0:
        return False
    else:
        for entity in entities:
            if entity['entity'] == 'detail':
                return True
        return False

# ask to continue to the next key
class Continue(Action):
    def name(self):
        return 'continue'

    def run(self, dispatcher, tracker, domain):
        global sessions
        # increment current index
        current_index = sessions[tracker.sender_id] + 1
        # find the next key
        next_key = get_next_kanban_key(current_index)
        # make it the current one
        current_key = next_key
        # if all themes are explained end the guide otherwise ask for the next one
        if not current_key:
            response = 'That is it for the crash course in kanban. Would you like to restart?'
            sessions[tracker.sender_id] = 0
        else:
            response = 'Would you like to know about ' + current_key + '?'
            sessions[tracker.sender_id] = current_index

        reply_options = [{"text": "yes"}, {"text": "no"}]

        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), None, response, reply_options, tracker.current_slot_values(),
                                          "kanban"))
        return []


class Explain(Action):
    def name(self):
        return 'explain'

    def run(self, dispatcher, tracker, domain):
        global sessions

        # get current intent
        intent = tracker.latest_message.parse_data['intent']['name']
        # get entities if any
        entities = tracker.latest_message.parse_data['entities']

        # check if entities exist and decide on the flow 
        if intent == 'switch_kanban' and len(entities) == 0:
            current_index = 0
            # get the first general key
            current_key = dict.kanban_general_keys[current_index]
        elif (intent == 'switch_kanban' and len(entities) > 0) or intent == 'inform':
            # get the current key from the user input
            current_key = tracker.get_slot('theme')
            # get the current index
            current_index = find_kanban_general_index(current_key)
        else:
            if tracker.sender_id in sessions:
                current_index = sessions[tracker.sender_id]
            else:
                current_index = 0
            # get the current key from the index
            current_key = dict.kanban_general_keys[current_index]

        try:
            current_detail_keys = dict.kanban_details_keys[current_index]
        except IndexError:
            current_detail_keys = None

        sessions[tracker.sender_id] = current_index

        # declare reply options
        reply_options = []
        # check if there available options and add them to the reply options
        if current_detail_keys is not None:
            for detail in current_detail_keys:
                reply_options.append({"text": detail})

        # explain the current key
        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), current_key, dict.kanban_general_keys_values[current_key],
                                          reply_options, tracker.current_slot_values(), "kanban"))
        return []


class ExplainDetail(Action):
    def name(self):
        return 'explain_detail'

    def run(self, dispatcher, tracker, domain):
        # get the detail entity from the one of the buttons offered as options in reply options above
        current_detail = tracker.get_slot('detail')
        # make sure the current index is the right one
        current_index = find_kanban_detail_index(current_detail)
        sessions[tracker.sender_id] = current_index
        # get the list of details based on the index
        current_detail_keys = dict.kanban_details_keys[current_index]
        # declare reply options
        reply_options = []
        # build the reply options while filtering out the current details
        for detail in current_detail_keys:
            if detail != current_detail:
                reply_options.append({"text": detail})
        # build the response based on the reply keys
        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), current_detail, dict.kanban_details_keys_values[current_detail],
                                          reply_options, tracker.current_slot_values(), "kanban"))
        return []
