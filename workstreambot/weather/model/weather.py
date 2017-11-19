

class Weather(object):
    # init method
    def __init__(self, weather_data):
        self._weather_data = weather_data

    # Parse the name of the city you are searching for
    def title(self):
        return self._weather_data['title']

    # Parse the description of the city you are searching for
    def description(self):
        return self._weather_data['description']

    # Parse the date when the weather was last retrieved
    def date(self):
        return self._weather_data['lastBuildDate']
