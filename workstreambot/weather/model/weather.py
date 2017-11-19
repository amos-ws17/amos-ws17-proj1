from .condition import Condition

class Weather(object):
    # init method
    def __init__(self, weather_data):
        self._weather_data = weather_data

    # Parse the name of the city
    def title(self):
        return self._weather_data['title']

    # Parse the description of the city
    def description(self):
        return self._weather_data['description']

    # Parse the date when the weather was last retrieved
    def date(self):
        return self._weather_data['lastBuildDate']

    # Parse the condition of the city
    def condition(self):
        return Condition(self._weather_data['item']['condition'])
