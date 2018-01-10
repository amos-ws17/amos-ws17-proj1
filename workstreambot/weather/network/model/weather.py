from .condition import Condition
from .forecast import Forecast


class Weather(object):
    # init method
    def __init__(self, weather_data):
        self._weather_data = weather_data

    # Parse the name of the city
    def getWeatherTitle(self):
        return self._weather_data['title']

    # Parse the description of the city
    def getWeatherDescription(self):
        return self._weather_data['description']

    # Parse the date when the weather was last retrieved
    def getLastUpdatedWeatherDate(self):
        return self._weather_data['lastBuildDate']

    # Parse the condition of the city
    def getWeatherConditionFactors(self):
        return Condition(self._weather_data['item']['condition'])

    # Parse the forecast for the upcoming days
    def getWeatherForecastFactors(self):
        forecasts = []
        [forecasts.append(Forecast(day)) for day in self._weather_data['item']['forecast']]
        return forecasts
