from datetime import datetime
from network.foursquareClient import FoursquareClient
from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionSearchSights(Action):
    
    def __init__(self):
        self.recNr = 0
        self.venues = []
    
    # the name should match the action to the utterance
    def name(self):
        return 'action_search_sights'
    # the run executes when the action is called
    def run(self, dispatcher, tracker, domain):
        # get the location and criteria entities from the console
        if (self.recNr == 0):
            location = tracker.get_slot('location')
            criteria = 'sights'
            if (str(tracker.get_slot('type_specific')) == 'None'):
                criteria = tracker.get_slot('type')
            else:
                criteria = tracker.get_slot('type_specific')
            # init the foursquare Client
            sightseeingClient = FoursquareClient()
            # fetch the sightseeing data
            self.venues = sightseeingClient.fetch_recommendations_for_city(str(location), str(criteria)) 
        v_id = self.venues[self.recNr].getRecommendedVenueId()
        v_name = self.venues[self.recNr].getRecommendedVenueName()
        v_contact = self.venues[self.recNr].getRecommendedVenueContact()
        v_address = self.venues[self.recNr].getRecommendedVenueAddress()
        v_price = self.venues[self.recNr].getRecommendedVenuePriceCategory()
        v_rating = self.venues[self.recNr].getRecommendedVenueRating()
        self.recNr += 1
        message = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' + v_address +  '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)                           
        dispatcher.utter_message(message)
        return [SlotSet("action_search_sights_result", message)]


