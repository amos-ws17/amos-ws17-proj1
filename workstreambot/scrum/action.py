from rasa_core.actions import Action

import json

# the themes that scrum can talk about, should be persisted in the DB
theme_list = ["scrum", "roles", "stories", "sprint", "ceremonies", "backlog", "estimations",
              "release", "burndown", "velocity", "extras", "spike", "goals"]
# the explanations of the themes
theme_dict = {"scrum": "", "roles": "PO, SM, DEV", "stories": "", "sprint": "", "ceremonies": "", "backlog": "",
              "estimations": "", "release": "", "burndown": "", "velocity": "", "extras": "",
              "spike": "", "goals": ""}

global current_theme = theme_list[0]


# get the next element to explain
def getNextElement(theme):
    current_index = theme_list.index(theme)
    try:
        current_index += 1
        return theme_list[current_index]
    except IndexError:
        return None


# ask to continue to the next theme
class ActionAskContinue(Action):
    def name(self):
        return 'utter_continue'

    def run(self, dispatcher, tracker, domain):
        # find the next theme
        next_theme = getNextElement(current_theme)
        # pass it to the global variable
        current_theme = next_theme

        data = {}
        data['slots'] = tracker.current_slot_values()

        # if all themes are explained end the guide otherwise ask for the next one
        if not next_theme:
            data['response'] = "That is it for the crash course in scrum"
        else:
            data['response'] = "Would you like to know about " + current_theme + "?"

        dispatcher.utter_message(json.dumps(data))
        return []


class ActionExplain(Action):
    def name(self):
        return 'utter_explain'

    def run(self, dispatcher, tracker, domain):
        # explain the current theme

        data = {}
        data['slots'] = tracker.current_slot_values()
        data['response'] = theme_dict[current_theme]

        dispatcher.utter_message(json.dumps(data))
        return []
