class Venue(object):
    # init method
    def __init__(self, venue_data):
        self._venue_data = venue_data

    # Parse the name of the city
    def getVenueName(self):
        return self._venue_data['name']
