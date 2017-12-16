from rasa_core.actions import Action

# the themes that scrum can talk about, should be persisted in the DB
theme_list = ["roles", "stories", "sprint", "ceremonies", "backlog", "estimations",
              "release", "burndown", "velocity", "extras", "spike", "goals"]
# the explanations of the themes
theme_dict = {"roles": "PO, SM, DEV", "stories": "", "sprint": "", "ceremonies": "", "backlog": "",
              "estimations": "", "release": "", "burndown": "", "velocity": "", "extras": "",
              "spike": "", "goals": ""}


# get the next element to explain
def getNextElement(theme):
    current_index = theme_list.index(theme)
    try:
        current_index += 1
        return theme_list[current_index]
    except IndexError:
        return ""

# ask to continue to the next theme
class ActionAskContinue(Action):
    def name(self):
        return 'utter_continue'

    def run(self, dispatcher, tracker, domain):
        # get the current theme
        current_theme = tracker.get_slot('theme')
        # find the next theme
        next_theme = getNextElement(current_theme)
        # if all themes are explained end the guide otherwise ask for the next one
        if not next_theme:
            dispatcher.utter_message("That is it for the crash course in scrum")
        else:
            dispatcher.utter_message("Would you like to know about " + next_theme + "?")
        return []

class ActionExplain(Action):
    def name(self):
        return 'utter_explain'

    def run(self, dispatcher, tracker, domain):
        # get the current theme
        current_theme = tracker.get_slot('theme')
        # explain the current theme 
        dispatcher.utter_message(theme_dict[current_theme])
        return []

class ActionEndGuide(Action):
    def name(self):
        return 'utter_end_guide'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("That is it for the crash course in scrum")
        return []
