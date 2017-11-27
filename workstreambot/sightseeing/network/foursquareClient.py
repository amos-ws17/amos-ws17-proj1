import foursquareConstants
import requests

class FoursquareClient(object):
    # define the base url for the API
    baseurl = foursquareConstants.foursquareGeneralKeys['Scheme'] + foursquareConstants.foursquareGeneralKeys['Host'] + foursquareConstants.foursquareGeneralKeys['Path']
    # function that gets the current weather for a given city
    def fetch_venues_for_city(self, city, venues):
        # define parameters
        parameters = {foursquareConstants.foursquareGeneralKeys['Client']: foursquareConstants.foursquareGeneralKeysValues['Client_ID'],
                      foursquareConstants.foursquareGeneralKeys['Secret']: foursquareConstants.foursquareGeneralKeysValues['Secret_ID'],
                      foursquareConstants.foursquareGeneralKeys['Version']: foursquareConstants.foursquareGeneralKeysValues['Version_ID'],
                      foursquareConstants.foursquareParamterKeys['Near']: city,
                      foursquareConstants.foursquareParamterKeys['Intent']: foursquareConstants.foursquareParamterKeysValues['Intent_ID'],
                      foursquareConstants.foursquareParamterKeys['Radius']: foursquareConstants.foursquareParamterKeysValues['Radius_ID'],
                      foursquareConstants.foursquareParamterKeys['Query']: venues,
                      foursquareConstants.foursquareParamterKeys['Limit']: foursquareConstants.foursquareParamterKeysValues['Limit_ID']}
        # add the method to the url
        searchURL = self.baseurl + foursquareConstants.foursquareMethodKeys['Search']
        # construct final url
        finalURL = requests.get(searchURL, params=parameters)
        print(finalURL.url)
