from datetime import datetime
from network.foursquareClient import FoursquareClient
from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionSearchSights(Action):
    # the name should match the action to the utterance
    def name(self):
        return 'action_search_sights'
    # the run executes when the action is called
    def run(self, dispatcher, tracker, domain):
        # get the location and criteria entities from the console
        location = tracker.get_slot('location')
        criteria = tracker.get_slot('type')
        # init the foursquare Client
        sightseeingClient = FoursquareClient()
        # fetch the sightseeing data
        venues = sightseeingClient.fetch_recommendations_for_city(str(location), str(criteria))
        message = 'No data could be found.'

        # get the venue factors
        for venue in venues:
            v_id = venue.getRecommendedVenueId()
            v_name = venue.getRecommendedVenueName()
            v_contact = venue.getRecommendedVenueContact()
            v_address = venue.getRecommendedVenueAddress()
            v_price = venue.getRecommendedVenuePriceCategory()
            v_rating = venue.getRecommendedVenueRating()
            message = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' +  '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)                           

        print(message)
        dispatcher.utter_message(message)
        return [SlotSet("action_search_sights_result", message)]
