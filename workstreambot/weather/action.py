

from rasa_core.actions import Action



class ActionSearchWeather(Action):
    # the name should match the action to the utterance
    def name(self):
        return 'action_search_weather'
    # the run executes when the action is called 
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Here's what the wheather looks like")
        return []
