import network.foursquareConstants as C
from network.apiClient import APIClient
from model.venue import Venue
from model.tips import Tips
from model.similar import Similar
from model.recommendation import Recommendation

class FoursquareClient(object):
    # define the base url for the API
    baseurl = C.foursquareGeneralKeys['Scheme'] + C.foursquareGeneralKeys['Host'] + C.foursquareGeneralKeys['Path']
    # define the base parameters for the API
    baseparameters = {C.foursquareGeneralKeys['Client']: C.foursquareGeneralKeysValues['Client_ID'],
                      C.foursquareGeneralKeys['Secret']: C.foursquareGeneralKeysValues['Secret_ID'],
                      C.foursquareGeneralKeys['Version']: C.foursquareGeneralKeysValues['Version_ID'],
                      C.foursquareParamterKeys['Limit']: C.foursquareParamterKeysValues['Limit_ID']}

    # function that gets the current venues matching a term for a given city
    def fetch_venues_for_city(self, city, venues):
        # define extra parameters
        extra = {C.foursquareParamterKeys['Near']: city,
                 C.foursquareParamterKeys['Intent']: C.foursquareParamterKeysValues['Intent_ID'],
                 C.foursquareParamterKeys['Radius']: C.foursquareParamterKeysValues['Radius_ID'],
                 C.foursquareParamterKeys['Query']: venues}
        # concatenate with base parameters
        parameters = dict(self.baseparameters)
        parameters.update(extra)
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

    # function that gets the venues matching a criteria for a given city
    def fetch_recommendations_for_city(self, city, criteria):
        # define extra parameters
        extra = {C.foursquareParamterKeys['Near']: city,
                 C.foursquareParamterKeys['Intent']: C.foursquareParamterKeysValues['Intent_ID'],
                 C.foursquareParamterKeys['Radius']: C.foursquareParamterKeysValues['Radius_ID'],
                 C.foursquareParamterKeys['Query']: criteria}
        # concatenate with base parameters
        parameters = dict(self.baseparameters)
        parameters.update(extra)
        # add the method to the url
        exploreURL = self.baseurl + C.foursquareMethodKeys['Explore']
        # init APIClient
        api = APIClient()
        # make the url call and retrieve a json Response
        jsonResponse = api.fetch(exploreURL, parameters)
        # check if the jsonResponse contains an object and pass it to the recommendation model
        if len(jsonResponse['response']['groups'][0]['items']) > 0:
            # empty array to store the recommendations dictionary
            recommendations = []
            # init a recommendation model with an object and pass that to the array
            [recommendations.append(Recommendation(place)) for place in jsonResponse['response']['groups'][0]['items']]
            # return the array of all recommendations models
            return recommendations
        else:
            # return the jsonResponse
            return jsonResponse


    # function that gets the current tips for a given venue
    def fetch_tips_for_venue(self, venue_id):
        # define parameters
        parameters = self.baseparameters
        # add the method to the url
        tipsURL = self.baseurl + C.foursquareMethodKeys['Venue_ID'] + venue_id + C.foursquareMethodKeys['Tips']
        # init APIClient
        api = APIClient()
        # make the url call and retrieve a json Response
        jsonResponse = api.fetch(tipsURL, parameters)
        # check if the jsonResponse contains an object and pass it to the tip model
        if int(jsonResponse['response']['tips']['count']) > 0:
            # empty array to store the tips dictionary
            tips = []
            # init a tip model with an object and pass that to the array
            [tips.append(Tips(tip)) for tip in jsonResponse['response']['tips']['items']]
            # return the array of all tips models
            return tips
        else:
            # return the jsonResponse
            return jsonResponse

    # function that gets the similar venues for a given venue
    def fetch_similar_for_venue(self, venue_id):
        # define parameters
        parameters = self.baseparameters
        # add the method to the url
        similarURL = self.baseurl + C.foursquareMethodKeys['Venue_ID'] + venue_id + C.foursquareMethodKeys['Similar']
        # init APIClient
        api = APIClient()
        # make the url call and retrieve a json Response
        jsonResponse = api.fetch(similarURL, parameters)
        # check if the jsonResponse contains an object and pass it to the similar model
        if int(jsonResponse['response']['similarVenues']['count']) > 0:
            # empty array to store the similar venues dictionary
            similar = []
            # init a tip model with an object and pass that to the array
            [similar.append(Similar(s)) for s in jsonResponse['response']['similarVenues']['items']]
            # return the array of all similar models
            return similar
        else:
            # return the jsonResponse
            return jsonResponse
