import requests

class yahooClient(object):
    # define the base Yahoo weather API URL
    baseurl = "https://query.yahooapis.com/v1/public/yql"

    # function that gets the current weather for a given city
    def fetch_weather_for_city(self, city):
        # the first s is substituted by the baseurl and the second s by the city paramater
        param = "?q=select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s')&format=json" % (city)
        # construct the final url by passing the paramaters and formatting the request
        finalURL = self.baseurl + param
        # make the url call and retrieve a json Response
        jsonResponse = self.fetch(finalURL)
        return jsonResponse


    # function that makes the call to the yahoo api
    def fetch(self, url):
        # get method
        r = requests.get(url)
        # check if you got a 200 response code
        if not r.ok:
            r.raise_for_status()
        # get the data response in json format
        data = r.json()
        # return the data
        return data
