from datetime import datetime
from network.foursquareClient import FoursquareClient
from rasa_core.actions import Action
import copy
from mongo_persistance.database_handler import MongoDBHandler

import json

class ActionPersisting(Action):
    def persist(self, data, conv_id):
        handler = MongoDBHandler(mongo_ip="mongo")
        handler.write_data(copy.deepcopy(data), conv_id, "sightseeingbot")

class ActionSearchSights(ActionPersisting):
    
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

        data = {}
        data['action_name'] = self.name()
        data['response'] = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' + v_address +  '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionGreet(ActionPersisting):
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
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []


class ActionGoodbye(ActionPersisting):
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
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []


class ActionAskHowCanIHelp(ActionPersisting):
    def name(self):
        return 'utter_ask_howcanhelp'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = 'How can I help you?'
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionAskLocation(ActionPersisting):
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
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionAskPrice(ActionPersisting):
    def name(self):
        return 'utter_ask_price'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = "Do you prefer cheap, moderately cheap, moderately expensive, expensive or does price matter to you?"
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionAckDoSearch(ActionPersisting):
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
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionSuggest(ActionPersisting):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = "Do you like it?"
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionFindAlternatives(ActionPersisting):
    def name(self):
        return 'utter_ack_findalternatives'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = "Ok let me see what else there is"
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionYoureWelcomed(ActionPersisting):
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
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []

class ActionAskHelpMore(ActionPersisting):
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
        self.persist(data, tracker.sender_id)

        dispatcher.utter_message(json.dumps(data))
        return []