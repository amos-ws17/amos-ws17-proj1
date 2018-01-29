import scrum.dictionary as dict
import utils as utils
from rasa_core.actions import Action

sessions = {}


def get_first_theme():
    for theme in dict.scrum:
        if dict.scrum[theme]['position'] == 1:
            return theme


def get_next_theme(current_theme):
    for theme in dict.scrum:
        if dict.scrum[theme]['position'] == dict.scrum[current_theme]['position'] + 1:
            return theme
    return None


def find_theme(current_detail):
    for theme in dict.scrum:
        if 'details' in dict.scrum[theme] and current_detail in dict.scrum[theme]['details']:
            return theme
    return None


# ask to continue to the next key
class Continue(Action):
    def name(self):
        return 'continue'

    def run(self, dispatcher, tracker, domain):
        global sessions

        next_theme = get_next_theme(sessions[tracker.sender_id])

        if not next_theme:
            content = 'That is it for the crash course in scrum. Would you like to restart?'
            sessions[tracker.sender_id] = get_first_theme()
        else:
            content = 'Would you like to know about ' + next_theme + '?'
            sessions[tracker.sender_id] = next_theme

        reply_options = [{"text": "yes", "reply": "yes"}, {"text": "no", "reply": "no"}]

        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), None, content, reply_options, tracker.current_slot_values(),
                                          "scrum"))
        return []


class Explain(Action):
    def name(self):
        return 'explain'

    def run(self, dispatcher, tracker, domain):
        global sessions

        intent = tracker.latest_message.parse_data['intent']['name']
        entities = tracker.latest_message.parse_data['entities']

        if intent == 'switch_scrum' and len(entities) == 0:
            current_theme = get_first_theme()
        elif (intent == 'switch_scrum' and len(entities) > 0) or intent == 'inform':
            current_theme = tracker.get_slot('theme')
        else:
            if tracker.sender_id in sessions:
                current_theme = sessions[tracker.sender_id]
            else:
                current_theme = get_first_theme()

        try:
            current_details = dict.scrum[current_theme]['details']
        except KeyError:
            current_details = None

        sessions[tracker.sender_id] = current_theme

        # declare reply options
        reply_options = []
        # check if there available options and add them to the reply options
        if current_details is not None:
            for key in current_details.keys():
                reply_options.append({"text": key, 'reply': key})

        # explain the current key
        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), current_theme, dict.scrum[current_theme]['general'],
                                          reply_options, tracker.current_slot_values(), "scrum"))
        return []


class ExplainDetail(Action):
    def name(self):
        return 'explain_detail'

    def run(self, dispatcher, tracker, domain):
        global sessions

        current_detail = tracker.get_slot('detail')
        current_theme = find_theme(current_detail)
        sessions[tracker.sender_id] = current_theme

        reply_options = []
        for key in dict.scrum[current_theme]['details']:
            if key != current_detail:
                reply_options.append({"text": key, "reply": key})

        dispatcher.utter_message(utils.prepare_action_response(self.name(), current_detail,
                                                               dict.scrum[current_theme]['details'][current_detail],
                                                               reply_options, tracker.current_slot_values(), "scrum"))
        return []
