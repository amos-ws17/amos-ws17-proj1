

from rasa_core.actions import Action



class ActionSearchWeather(Action):
    def name(self):
        return 'action_search_weather'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what the wheather looks like")
        return []
