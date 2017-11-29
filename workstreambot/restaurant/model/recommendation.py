class Recommendation(object):
    # init method
    def __init__(self, explore_data):
        self._explore_data = explore_data

    # Parse the id of the recommended venue
    def getRecommendedVenueId(self):
        return self._explore_data['venue']['id']

    # Parse the name of the recommended venue
    def getRecommendedVenueName(self):
        return self._explore_data['venue']['name']

    # Parse the contact of the recommended venue
    def getRecommendedVenueContact(self):
        if 'phone' in self._explore_data['venue']['contact']:
            return self._explore_data['venue']['contact']['phone']
        return ("No Contact available")

    # Parse the address of the recommended venue
    def getRecommendedVenueAddress(self):
        if 'location' in self._explore_data['venue']:
            return self._explore_data['venue']['location']['address']
        return ("No address category available")
        

    # Parse the price category of the recommended venue
    def getRecommendedVenuePriceCategory(self):
        if 'price' in self._explore_data['venue']:
            return self._explore_data['venue']['price']['message']
        return ("No price category available")

    # Parse the rating of the recommended venue
    def getRecommendedVenueRating(self):
        return self._explore_data['venue']['rating']
