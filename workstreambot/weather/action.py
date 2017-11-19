import time
from network.yahooClient import YahooClient
from rasa_core.actions import Action



class ActionSearchWeather(Action):
    # the name should match the action to the utterance
    def name(self):
        return 'action_search_weather'
    # the run executes when the action is called
    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('location')
        date = tracker.get_slot('date')

        weatherClient = YahooClient()
        print(weatherClient.fetch_weather_for_city(str(location)))

        if str(date) == "None":
           date = time.strftime("%d-%m-%Y")

        dispatcher.utter_message("Here's what the wheather looks like in " + str(location) + " on " + str(date))
        return []
