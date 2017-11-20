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
           description = weather.getWeatherDescription()
           condition = weather.getWeatherConditionFactors()
           conditionDesc = condition.getConditionDescription()
           conditionTemp = condition.getConditionCurrentTemperature()
           conditionDate = condition.getLastUpdatedConditionDate()
           dispatcher.utter_message(description + '\n' + "It is " + conditionDesc + '\n' + "The currrent temperature is " + conditionTemp + ' C\n' + "Last updated " + conditionDate)
        else:
           date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
           for num in range(0, len(weather.getWeatherForecastFactors())):
              forecast = weather.getWeatherForecastFactors()[num]
              if date.strftime('%d %b %Y') == forecast.getLastUpdatedForecastDate():
                 # get the weather factors
                 description = weather.description()
                 forecastDesc = forecast.getForecastDescription()
                 forecastHigh = forecast.getForecastHighTemperature()
                 forecastLow = forecast.getForecastLowTemperature()
                 forecastDate = forecast.getLastUpdatedForecastDate()
                 dispatcher.utter_message(description + ' on ' + forecastDate + '\n' + "It is " + forecastDesc + '\n' + "The temperature is between " + forecastLow + ' and ' + forecastHigh)

        return []
