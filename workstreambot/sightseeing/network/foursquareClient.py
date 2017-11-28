import network.foursquareConstants as C
from network.apiClient import APIClient
from model.venue import Venue
from model.tips import Tips

class FoursquareClient(object):
    # define the base url for the API
    baseurl = C.foursquareGeneralKeys['Scheme'] + C.foursquareGeneralKeys['Host'] + C.foursquareGeneralKeys['Path']
    # function that gets the current venues for a given city
    def fetch_venues_for_city(self, city, venues):
        # define parameters
        parameters = {C.foursquareGeneralKeys['Client']: C.foursquareGeneralKeysValues['Client_ID'],
                      C.foursquareGeneralKeys['Secret']: C.foursquareGeneralKeysValues['Secret_ID'],
                      C.foursquareGeneralKeys['Version']: C.foursquareGeneralKeysValues['Version_ID'],
                      C.foursquareParamterKeys['Near']: city,
                      C.foursquareParamterKeys['Intent']: C.foursquareParamterKeysValues['Intent_ID'],
                      C.foursquareParamterKeys['Radius']: C.foursquareParamterKeysValues['Radius_ID'],
                      C.foursquareParamterKeys['Query']: venues,
                      C.foursquareParamterKeys['Limit']: C.foursquareParamterKeysValues['Limit_ID']}
        # add the method to the url
        searchURL = self.baseurl + C.foursquareMethodKeys['Search']
        # init APIClient
        api = APIClient()
        # make the url call and retrieve a json Response
        jsonResponse = api.fetch(searchURL, parameters)
        # check if the jsonResponse contains an object and pass it to the venue model
        if len(jsonResponse['response']['venues']) > 0:
            # empty array to store the venues dictionary
            venues = []
            # init a venue model with an object and pass that to the array
            [venues.append(Venue(place)) for place in jsonResponse['response']['venues']]
            # return the array of all venue models
            return venues
        else:
            # return the jsonResponse
            return jsonResponse

    def fetch_tips_for_venue(self, venue_id):
        # define parameters
        parameters = {C.foursquareGeneralKeys['Client']: C.foursquareGeneralKeysValues['Client_ID'],
                      C.foursquareGeneralKeys['Secret']: C.foursquareGeneralKeysValues['Secret_ID'],
                      C.foursquareGeneralKeys['Version']: C.foursquareGeneralKeysValues['Version_ID'],
                      C.foursquareParamterKeys['Limit']: C.foursquareParamterKeysValues['Limit_ID']}
        # add the method to the url
        tipsURL = self.baseurl + C.foursquareMethodKeys['Venue_ID'] + venue_id + C.foursquareMethodKeys['Tips']
        # init APIClient
        api = APIClient()
        # make the url call and retrieve a json Response
        jsonResponse = api.fetch(tipsURL, parameters)
        # check if the jsonResponse contains an object and pass it to the weather model
        if int(jsonResponse['response']['tips']['count']) > 0:
            # empty array to store the tips dictionary
            tips = []
            # init a tip model with an object and pass that to the array
            [tips.append(Tips(tip)) for tip in jsonResponse['response']['tips']['items']]
            # return the array of all venue models
            return tips
        else:
            # return the jsonResponse
            return jsonResponse
