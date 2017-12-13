from datetime import datetime
from network.foursquareClient import FoursquareClient
from rasa_core.actions import Action
import copy

import json

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
        data = {}
        data['response'] = 'No data could be found.'
        # get the venue factors
        for venue in venues:
            v_id = venue.getRecommendedVenueId()
            v_name = venue.getRecommendedVenueName()
            v_contact = venue.getRecommendedVenueContact()
            v_address = venue.getRecommendedVenueAddress()
            v_price = venue.getRecommendedVenuePriceCategory()
            v_rating = venue.getRecommendedVenueRating()
            data['response'] = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' + v_address + '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)


        data['action_name'] = self.name()
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionGreet(Action):
    def name(self):
        return 'utter_greet'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = 'Hey there!'
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        dispatcher.utter_message(json.dumps(data))
        return []


class ActionGoodbye(Action):
    def name(self):
        return 'utter_goodbye'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = 'Bye-bye'
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionAskLocation(Action):
    def name(self):
        return 'utter_ask_location'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = "Where do you want me to search?"
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionAskCuisine(Action):
    def name(self):
        return 'utter_ask_cuisine'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()
        data['response'] = "What kind of cuisine would you like and in which price range should it be? (cheap, expensive)"
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        #buttons:
        #- title: "cheap"
        #  payload: "cheap"
        #- title: "expensive"
        #  payload: "expensive"

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionAckDoSearch(Action):
    def name(self):
        return 'utter_ack_dosearch'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = "Ok let me see what I can find."
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionOnIt(Action):
    def name(self):
        return 'utter_on_it'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = "I'm on it"
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionYoureWelcomed(Action):
    def name(self):
        return 'utter_yourewelcomed'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = "I am happy to assist you. have a nice day!"
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionAskHelpMore(Action):
    def name(self):
        return 'utter_ask_helpmore'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = "Is there anything more that I can help with?"
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        

        dispatcher.utter_message(json.dumps(data))
        return []



		
