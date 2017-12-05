from datetime import datetime
from network.yahooClient import YahooClient
from rasa_core.actions import Action

import json

class ActionAskCuisine(Action):
    def name(self):
        return 'utter_ask_cuisine'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = 'What kind of cuisine would you like?'
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()

        dispatcher.utter_message(json.dumps(data))
        return []
