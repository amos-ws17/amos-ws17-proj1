from rasa_core.actions import Action

import json

def prepareResponseJson(action_name, response, tracker):
    data = {}
    data['action_name'] = action_name
    data['response'] = response
    data['slots'] = tracker.current_slot_values()
    data['sender'] = tracker.sender_id
    data['message'] = tracker.latest_message.parse_data
    data['paused'] = tracker.is_paused()

    return json.dumps(data)

class UtterGreet(Action):
    def name(self):
        return 'utter_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Hey there!', tracker))
        return []

class UtterAskHowCanHelp(Action):
    def name(self):
        return 'utter_ask_how_can_help'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'How can I help you?', tracker))
        return []

class UtterAskCuisine(Action):
    def name(self):
        return 'utter_ask_cuisine'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'What kind of cuisine would you like?', tracker))
        return []

class UtterAskLocation(Action):
    def name(self):
        return 'utter_ask_location'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Please enter the city youre interested in.', tracker))
        return []

class UtterAskPrice(Action):
    def name(self):
        return 'utter_ask_price'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'In which price range (cheap, moderately cheap, moderately expensive, expensive) should it be?', tracker))
        return []

class UtterAckDoSearch(Action):
    def name(self):
        return 'utter_ack_do_search'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Ok let me see what I can find.', tracker))
        return []

class ActionSuggestRestaurant(Action):
    def name(self):
        return 'action_suggest_restaurant'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Thats what I found. (restaurant)', tracker))
        return []

class ActionSuggestSights(Action):
    def name(self):
        return 'action_suggest_sights'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Thats what I found. (sights)', tracker))
        return []

class ActionSuggestWeather(Action):
    def name(self):
        return 'action_suggest_weather'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Thats what I found. (weather)', tracker))
        return []

class UtterLikeIt(Action):
    def name(self):
        return 'utter_like_it'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Do you like it?', tracker))
        return []

class ActionFindAlternativeRestaurant(Action):
    def name(self):
        return 'action_find_alternative_restaurant'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Maybe this is better. (restaurant)', tracker))
        return []

class ActionFindAlternativeSight(Action):
    def name(self):
        return 'action_find_alternative_sight'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Maybe this is better. (sight)', tracker))
        return []

class UtterAskHelpMore(Action):
    def name(self):
        return 'utter_ask_help_more'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Is there anything more that I can help with?', tracker))
        return []

class UtterYoureWelcomed(Action):
    def name(self):
        return 'utter_youre_welcomed'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'I am happy to assist you. Have a nice day!', tracker))
        return []

class UtterGoodbye(Action):
    def name(self):
        return 'utter_goodbye'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(prepareResponseJson(self.name(), 'Goodbye', tracker))
        return []
