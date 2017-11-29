from datetime import datetime
from network.foursquareClient import FoursquareClient
from rasa_core.actions import Action
from rasa_core.events import SlotSet



class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        # init the foursquare Client
        restaurantClient = FoursquareClient()

        venues = restaurantClient.fetch_recommendations_for_city(str(location), str(price), str(cuisine))
        message = 'No data could be found.'
        # get the venue factors
        for venue in venues:
            v_id = venue.getRecommendedVenueId()
            v_name = venue.getRecommendedVenueName()
            v_contact = venue.getRecommendedVenueContact()
            v_address = venue.getRecommendedVenueAddress()
            v_price = venue.getRecommendedVenuePriceCategory()
            v_rating = venue.getRecommendedVenueRating()
            message = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' + v_address + '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)
        print(message)
        dispatcher.utter_message(message)
        return [SlotSet("action_suggest_result", message)]


		
