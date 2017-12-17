from rasa_core.actions import Action

import json

# the themes that scrum can talk about, should be persisted in the DB
theme_list = ["scrum", "roles", "stories", "sprint", "ceremonies", "backlog", "estimations",
              "release", "burndown", "velocity", "extras", "spike", "goals"]
# the explanations of the themes
theme_dict = {"scrum": "", "roles": "PO, SM, DEV", "stories": "", "sprint": "", "ceremonies": "", "backlog": "",
              "estimations": "", "release": "", "burndown": "", "velocity": "", "extras": "",
              "spike": "", "goals": ""}

current_theme = theme_list[0]


# get the next element to explain
def getNextElement(theme):
    current_index = theme_list.index(theme)
    try:
        current_index += 1
        return theme_list[current_index]
    except IndexError:
        return None


def getResponse(action_name, tracker, response):
    data = {}
    data['action_name'] = action_name
    data['paused'] = tracker.is_paused()
    data['slots'] = tracker.current_slot_values()
    data['dialogue_message'] = tracker.latest_message.parse_data
    data['response'] = response

    return json.dumps(data)

# ask to continue to the next theme
class ActionContinue(Action):
    def name(self):
        return 'utter_continue'

    def run(self, dispatcher, tracker, domain):
        global current_theme

        # find the next theme
        next_theme = getNextElement(current_theme)
        # pass it to the global variable
        current_theme = next_theme

        # if all themes are explained end the guide otherwise ask for the next one
        if not next_theme:
            response = "That is it for the crash course in scrum. Would you like to restart?"
            current_theme = theme_list[0]
        else:
            response = "Would you like to know about " + current_theme + "?"

        dispatcher.utter_message(getResponse(self.name(), tracker, response))
        return []


class ActionExplain(Action):
    def name(self):
        return 'utter_explain'

    def run(self, dispatcher, tracker, domain):
        global current_theme

        if tracker.latest_message.parse_data['intent']['name'] == 'inform_scrum':
            current_theme = theme_list[0]

        # explain the current theme
        dispatcher.utter_message(getResponse(self.name(), tracker, theme_dict[current_theme]))
        return []
