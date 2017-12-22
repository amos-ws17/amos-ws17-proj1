from .apiClient import APIClient
from weather.model.weather import Weather

class YahooClient(object):
    # define the base url for the API
    baseurl = "https://query.yahooapis.com"
    # define the path 
    path = "/v1/public/yql"

    # function that gets the current weather for a given city
    def fetch_weather_for_city(self, city):
        # define paramater with string formatting where the s is substituted by the city paramater
        query = "?q=select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s')and u='c'&format=json" % (city)
        # construct the final url by passing the paramaters and formatting the request
        finalURL = self.baseurl + self.path + query
        # init APIClient
        api = APIClient()
        # make the url call and retrieve a json Response
        jsonResponse = api.fetch(finalURL)
        # check if the jsonResponse contains an object and pass it to the weather model
        if int(jsonResponse['query']['count']) > 0:
            # init Weather
            weatherModel = Weather(jsonResponse['query']['results']['channel'])
            # return the weather model
            return weatherModel
        else:
            # return the json response
            return jsonResponse
