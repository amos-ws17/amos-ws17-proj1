from datetime import datetime
from network.yahooClient import YahooClient
from rasa_core.actions import Action

import locale
import utils


class ActionAskLocation(Action):
    def name(self):
        return 'utter_ask_location'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            utils.prepare_action_response(self.name(), tracker, 'Please enter the city you`re interested in.'))
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
        weather_client = YahooClient()
        # fetch the weather data
        weather = weather_client.fetch_weather_for_city(str(location))

        response = 'No data could be found.'

        if str(date) == 'None':
            # get the weather factors
            description = weather.getWeatherDescription()
            condition = weather.getWeatherConditionFactors()
            condition_desc = condition.getConditionDescription()
            condition_temp = condition.getConditionCurrentTemperature()
            condition_date = condition.getLastUpdatedConditionDate()

            response = description + '\nCondition: ' + condition_desc + '\nThe currrent temperature is ' + condition_temp + ' degree\nLast updated ' + condition_date
        else:
            locale.setlocale(locale.LC_ALL, 'en_US.utf8')
            date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
            for num in range(0, len(weather.getWeatherForecastFactors())):
                forecast = weather.getWeatherForecastFactors()[num]
                forecast_date = forecast.getLastUpdatedForecastDate()
                if date.strftime('%d %b %Y') == forecast_date:
                    # get the weather factors
                    description = weather.getWeatherDescription()
                    forecast_desc = forecast.getForecastDescription()
                    forecast_high = forecast.getForecastHighTemperature()
                    forecast_low = forecast.getForecastLowTemperature()

                    response = description + ' on ' + forecast_date + '\nCondition: ' + forecast_desc + '\nThe temperature is between ' + forecast_low + ' and ' + forecast_high + ' degree'

        dispatcher.utter_message(utils.prepare_action_response(self.name(), tracker, response))
        return []
