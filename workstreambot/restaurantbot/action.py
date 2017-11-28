from datetime import datetime
from network.foursquareClient import FoursquareClient
from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionSuggest(Action):
    # the name should match the action to the utterance
    def name(self):
        return 'action_suggest'
    # the run executes when the action is called
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("papi's pizza place. it's a pretty guuda")
        return []
