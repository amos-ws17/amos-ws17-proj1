from datetime import datetime
from network.yahooClient import YahooClient
from rasa_core.actions import Action

import utils


class ActionAskLocation(Action):
    def name(self):
        return 'utter_ask_location'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(utils.getResponse(self.name(), tracker, 'Please enter the city you`re interested in.'))
        return []


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

        response = 'No data could be found.'

        if str(date) == 'None':
           # get the weather factors
           description = weather.getWeatherDescription()
           condition = weather.getWeatherConditionFactors()
           conditionDesc = condition.getConditionDescription()
           conditionTemp = condition.getConditionCurrentTemperature()
           conditionDate = condition.getLastUpdatedConditionDate()

           response = description + '\nCondition: ' + conditionDesc + '\nThe currrent temperature is ' + conditionTemp + ' degree\nLast updated ' + conditionDate
        else:
           date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
           for num in range(0, len(weather.getWeatherForecastFactors())):
              forecast = weather.getWeatherForecastFactors()[num]
              if date.strftime('%d %b %Y') == forecast.getLastUpdatedForecastDate():
                 # get the weather factors
                 description = weather.getWeatherDescription()
                 forecastDesc = forecast.getForecastDescription()
                 forecastHigh = forecast.getForecastHighTemperature()
                 forecastLow = forecast.getForecastLowTemperature()
                 forecastDate = forecast.getLastUpdatedForecastDate()

                 response = description + ' on ' + forecastDate + '\nCondition: ' + forecastDesc + '\nThe temperature is between ' + forecastLow + ' and ' + forecastHigh + ' degree'

        dispatcher.utter_message(utils.getResponse(self.name(), tracker, response))
        return []
