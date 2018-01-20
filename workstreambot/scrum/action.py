from rasa_core.actions import Action

import utils

current_theme = theme_list[0]
current_detail = detail_list[0]


# get the next element to explain
def getNextThemeElement(theme):
    current_index = theme_list.index(theme)
    try:
        current_index += 1
        return theme_list[current_index]
    except IndexError:
        return None

def getNextDetailElement(detail):
    current_index = theme_list.index(detail)
    try:
        current_index += 1
        return detail_list[current_index]
    except IndexError:
        return None


# ask to continue to the next theme
class Continue(Action):
    def name(self):
        return 'continue'

    def run(self, dispatcher, tracker, domain):
        global current_theme

        # find the next theme
        next_theme = getNextThemeElement(current_theme)
        # pass it to the global variable
        current_theme = next_theme

        # if all themes are explained end the guide otherwise ask for the next one
        if not next_theme:
            response = 'That is it for the crash course in scrum. Would you like to restart?'
            current_theme = theme_list[0]
        else:
            response = 'Would you like to know about ' + current_theme + '?'

        dispatcher.utter_message(utils.prepare_action_response(self.name(), tracker, response))
        return []


class Explain(Action):
    def name(self):
        return 'explain'

    def run(self, dispatcher, tracker, domain):
        global current_theme

        if tracker.latest_message.parse_data['intent']['name'] == 'switch_scrum':
            current_theme = theme_list[0]

        # explain the current theme
        dispatcher.utter_message(utils.prepare_action_response(self.name(), tracker, theme_dict[current_theme]))
        return []


# ask to continue to the next detailed information
class ContinueDetail(Action):
    def name(self):
        return 'continue_detail'

    def run(self, dispatcher, tracker, domain):
        global current_detail

        # find the next detail
        next_detail = getNextDetailElement(current_detail)
        # pass it to the global variable
        current_detail = next_detail

        # if all details are explained end the guide otherwise ask for the next one
        if not next_detail:
            response = 'That is it for the crash course regarding this aspect. Would you like to restart?'
            current_detail = detail_list[0]
        else:
            response = 'Would you like to know about ' + current_detail + '?'

        dispatcher.utter_message(utils.prepare_action_response(self.name(), tracker, response))
        return []


class ExplainDetail(Action):
    def name(self):
        return 'explain_detail'

    def run(self, dispatcher, tracker, domain):
        global current_detail

        if tracker.latest_message.parse_data['intent']['name'] == 'switch_scrum':
            current_detail = detail_list[0]

        # explain the current detail
        dispatcher.utter_message(utils.prepare_action_response(self.name(), tracker, theme_dict[current_detail]))
        return []
