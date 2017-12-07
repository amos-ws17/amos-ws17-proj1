class Venue(object):
    # init method
    def __init__(self, venue_data):
        self._venue_data = venue_data

    # Parse the id of the venue
    def getVenueId(self):
        return self._venue_data['id']

    # Parse the name of the venue
    def getVenueName(self):
        return self._venue_data['name']

    # Parse the contact of the venue
    def getVenueContact(self):
        if 'phone' in self._venue_data['contact']:
            return self._venue_data['contact']['phone']
        return ("No Contact available")

    # Parse the address of the venue
    def getVenueAddress(self):
        return self._venue_data['location']['formattedAddress']

    # Parse the website of the venue
    def getVenueWebsite(self):
        return self._venue_data['url'] 
