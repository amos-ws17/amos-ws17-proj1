class Similar(object):
    # init method
    def __init__(self, similar_data):
        self._similar_data = similar_data

    # Parse the id of the similar venue
    def getSimilarVenueId(self):
        return self._similar_data['id']

    # Parse the name of the simlar venue
    def getSimilarVenueName(self):
        return self._similar_data['name']

    # Parse the contact of the similar venue
    def getSimilarVenueContact(self):
        if 'phone' in self._similar_data['contact']:
            return self._similar_data['contact']['phone']
        return ("No Contact available")

    # Parse the address of the similar venue
    def getSimilarVenueAddress(self):
        return self._similar_data['location']['formattedAddress']

    # Parse the website of the similar venue
    def getSimilarVenueWebsite(self):
        return self._similar_data['url']
