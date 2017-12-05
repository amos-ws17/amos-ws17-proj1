from datetime import datetime
from network.yahooClient import YahooClient
from rasa_core.actions import Action

import json

class ActionYoureWelcomed(Action):
    def name(self):
        return 'utter_youre_welcomed'

    def run(self, dispatcher, tracker, domain):
        data = {}
        data['action_name'] = self.name()

        data['response'] = 'I am happy to assist you. Have a nice day!'
        data['slots'] = tracker.current_slot_values()
        data['sender'] = tracker.sender_id
        data['message'] = tracker.latest_message.parse_data
        data['paused'] = tracker.is_paused()

        dispatcher.utter_message(json.dumps(data))
        return []
