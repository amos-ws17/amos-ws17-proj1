import time
from network.yahooClient import YahooClient
from rasa_core.actions import Action



class ActionSearchWeather(Action):
    # the name should match the action to the utterance
    def name(self):
        return 'action_search_weather'
    # the run executes when the action is called
    def run(self, dispatcher, tracker, domain):
        # get the location entity from the console
        location = tracker.get_slot('location')
        # init the weather Client
        weatherClient = YahooClient()
        # fetch the weather data
        weather = weatherClient.fetch_weather_for_city(str(location))
        # get the weather factors
        title = weather.text()
        condition = weather.condition()
        conditionTitle = condition.text()
        conditionTemp = condition.temp()
        conditionDate = condition.date()

        #if str(date) == "None":
           #date = time.strftime("%d-%m-%Y")

        dispatcher.utter_message(title + '\n' + "It is " + conditionTitle + '\n' + "The currrent temperature is " + conditionTemp + '\n' + "Last updated " + conditionDate)
        return []
