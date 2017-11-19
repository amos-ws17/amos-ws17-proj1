import requests

class yahooClient(object):
    # define the base Yahoo weather API URL
    baseurl = "https://query.yahooapis.com/v1/public/yql"

    # function that gets the current weather for a given city
    def fetch_weather_for_city(self, city):
        # define paramater with string formatting where the s is substituted by the city paramater
        param = "?q=select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s')&format=json" % (city)
        # construct the final url by passing the paramaters and formatting the request
        finalURL = self.baseurl + param
        # make the url call and retrieve a json Response
        jsonResponse = self.fetch(finalURL)
        # return the json response
        return jsonResponse


    # function that makes the call to the yahoo api
    def fetch(self, url):
        # get method
        r = requests.get(url)
        # check if you got a 200 response code
        if not r.ok:
            r.raise_for_status()
        # check if the reponse body contains data
        if not r.text:
            print("No data was returned")
        # check the data response is in json format
        try:
            data = r.json()
        except ValueError:
            print("The data is not in JSON format")
        # check that the json method did not return an empty dictionary
        if not data:
            print("Empty dictionary was returned from the json serialization")
        # return the data
        return data
