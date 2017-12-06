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
                      C.foursquareParameterKeys['Limit']: C.foursquareParameterKeysValues['Limit_ID']}
                      
    # function that converts price to a number
    def convert_price(self, price):
        if (price == 'cheap'):
            return 1
        elif (price == 'expensive'):
            return 3
        elif (price == 'very expensive'):
            return 4
        elif (price == 'moderately cheap'):
            return 2



    # function that gets the venues matching a criteria for a given city
    def fetch_restaurant_for_city(self, city, price, cuisine):
        # define extra parameters
        extra = {C.foursquareParameterKeys['Near']: city,
				C.foursquareParameterKeys['Radius']: C.foursquareParameterKeysValues['Radius_ID'],
				C.foursquareParameterKeys['Query']: cuisine,
				C.foursquareParameterKeys['Price']: self.convert_price(price)}
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

    # function that gets the venues matching a criteria for a given city
    def fetch_sights_for_city(self, city, criteria):
        # define extra parameters
        extra = {C.foursquareParameterKeys['Near']: city,
                 C.foursquareParameterKeys['Intent']: C.foursquareParameterKeysValues['Intent_ID'],
                 C.foursquareParameterKeys['Radius']: C.foursquareParameterKeysValues['Radius_ID'],
                 C.foursquareParameterKeys['Query']: criteria}
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

