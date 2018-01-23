import scrum.scrumConstants as S
import utils as utils
from rasa_core.actions import Action

current_index = 0


# get the next key to explain
def getNextScrumKey(index):
    try:
        key = S.scrumGeneralKeys[index]
        return key
    except IndexError:
        return None


# find a specific key to explain
def findScrumKey(key):
    scrum_key = ""
    if key in S.scrumGeneralKeysValues:
        scrum_key = key
        return scrum_key
    elif key in S.scrumDetailsKeysValues:
        scrum_key = key
        return key
    else:
        return None

def findScrumDetailIndex(key):
    for details in S.scrumDetailsKeys:
        if key in details:
            return S.scrumDetailsKeys.index[details]
    return None


# ask to continue to the next key
class Continue(Action):
    def name(self):
        return 'continue'

    def run(self, dispatcher, tracker, domain):
        global current_index
        # increment current index
        current_index += 1
        # find the next key
        next_key = getNextScrumKey(current_index)
        # make it the current one
        current_key = next_key
        # if all themes are explained end the guide otherwise ask for the next one
        if not current_key:
            response = 'That is it for the crash course in scrum. Would you like to restart?'
            current_index = 0
        else:
            response = 'Would you like to know about ' + current_key + '?'

        reply_options = [{"text": "yes"}, {"text": "no"}]

        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), None, response, reply_options, tracker.current_slot_values(),
                                          "scrum"))
        return []


class Explain(Action):
    def name(self):
        return 'explain'

    def run(self, dispatcher, tracker, domain):
        global current_index

        if tracker.latest_message.parse_data['intent']['name'] == 'switch_scrum':
            current_key = S.scrumGeneralKeys[0]
            current_detail_keys = S.scrumDetailsKeys[0]
        elif tracker.latest_message.parse_data['intent']['name'] == 'inform':
            # TODO
            current_key = S.scrumGeneralKeys[current_index]
            current_detail_keys = S.scrumDetailsKeys[current_index]
        else:
            current_key = S.scrumGeneralKeys[current_index]
            current_detail_keys = S.scrumDetailsKeys[current_index]

        # declare reply options
        reply_options = []
        # check if there available options and add them to the reply options
        for detail in current_detail_keys:
            reply_options.append({"text": detail})

        # explain the current key
        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), current_key, S.scrumGeneralKeysValues[current_key],
                                          reply_options,
                                          tracker.current_slot_values(), "scrum"))
        return []


class ExplainDetail(Action):
    def name(self):
        return 'explain_detail'

    def run(self, dispatcher, tracker, domain):
        global current_index

        # get the detail entity from the one of the buttons offered as options in reply options above
        current_detail = tracker.get_slot('detail')
        # make sure the current index is the right one
        current_index = findScrumDetailIndex(current_detail)
        # get the list of details based on the index
        current_detail_keys = S.scrumDetailsKeys[current_index]
        # declare reply options
        reply_options = []
        # build the reply options while filtering out the current details
        for detail in current_detail_keys:
            if detail != current_detail:
                reply_options.append({"text": detail})
        # build the response based on the reply keys
        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), current_detail, S.scrumDetailsKeysValues[current_detail],
                                          reply_options, tracker.current_slot_values(), "scrum"))
        return []
