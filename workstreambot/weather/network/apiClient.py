import requests


class APIClient(object):
    # function that makes the call to an api
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
