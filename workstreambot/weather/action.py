from datetime import datetime
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
        date = tracker.get_slot('time')
        # init the weather Client
        weatherClient = YahooClient()
        # fetch the weather data
        weather = weatherClient.fetch_weather_for_city(str(location))
        

        if str(date) == "None":
           # get the weather factors
           description = weather.description()
           condition = weather.condition()
           conditionTitle = condition.text()
           conditionTemp = condition.temp()
           conditionDate = condition.date()
           dispatcher.utter_message(description + '\n' + "It is " + conditionTitle + '\n' + "The currrent temperature is " + conditionTemp + ' C\n' + "Last updated " + conditionDate)
        else:
           date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
           for num in range(0, len(weather.forecast())):
              forecast = weather.forecast()[num]
              if date.strftime('%d %b %Y') == forecast.date():
                 # get the weather factors
                 description = weather.description()
                 forecastTitle = forecast.text()
                 forecastHigh = forecast.high()
                 forecastLow = forecast.low()
                 forecastDate = forecast.date()
                 dispatcher.utter_message(description + ' on ' + forecastDate + '\n' + "It is " + forecastTitle + '\n' + "The temperature is between " + forecastLow + ' and ' + forecastHigh)

        return []
