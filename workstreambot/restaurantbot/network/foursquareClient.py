import network.foursquareConstants as C
from network.apiClient import APIClient
from model.venue import Venue
from model.tips import Tips
from model.similar import Similar
from model.recommendation import Recommendation

#import foursquareConstants as C
#from apiClient import APIClient

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
            return 4
        elif (price == 'moderately expensive'):
            return 3
        elif (price == 'moderately cheap'):
            return 2



    # function that gets the venues matching a criteria for a given city
    def fetch_recommendations_for_city(self, city, price, cuisine):
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
        print (exploreURL)
        print (parameters)
        # make the url call and retrieve a json Response
        jsonResponse = api.fetch(exploreURL, parameters)
        
        print (jsonResponse)
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

    

#restaurantClient = FoursquareClient()
#venues = restaurantClient.fetch_recommendations_for_city('berlin', 'cheap', 'italian')
