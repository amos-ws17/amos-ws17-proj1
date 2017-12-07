from datetime import datetime
from network.yahooClient import YahooClient
from network.foursquareClient import FoursquareClient
from rasa_core.actions import Action

import json

restaurants = None
restaurantsCounter = 0
sights = None
sightsCounter = 0

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
        location = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        # init the foursquare Client
        restaurantClient = FoursquareClient()

        global restaurants
        global restaurantsCounter
        restaurants = restaurantClient.fetch_restaurant_for_city(str(location), str(price), str(cuisine))
        restaurantsCounter = 0

        message = 'No data could be found.'
        # get the venue factors
        if len(restaurants) > 0:
            v_name = restaurants[0].getRecommendedVenueName()
            v_contact = restaurants[0].getRecommendedVenueContact()
            v_address = restaurants[0].getRecommendedVenueAddress()
            v_price = restaurants[0].getRecommendedVenuePriceCategory()
            v_rating = restaurants[0].getRecommendedVenueRating()
            message = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' + v_address + '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)

        dispatcher.utter_message(prepareResponseJson(self.name(), message, tracker))
        return []

class ActionSuggestSights(Action):
    def name(self):
        return 'action_suggest_sights'

    def run(self, dispatcher, tracker, domain):
        # get the location and criteria entities from the console
        location = tracker.get_slot('location')
        criteria = 'sights'
        if (str(tracker.get_slot('type_specific')) == 'None'):
            criteria = tracker.get_slot('type')
        else:
            criteria = tracker.get_slot('type_specific')

        sightseeingClient = FoursquareClient()

        global sights
        global sightsCounter
        sights = sightseeingClient.fetch_sights_for_city(str(location), str(criteria))
        sightsCounter = 0

        message = 'No data could be found.'
        if len(sights) > 0:
            v_name = sights[0].getRecommendedVenueName()
            v_contact = sights[0].getRecommendedVenueContact()
            v_address = sights[0].getRecommendedVenueAddress()
            v_price = sights[0].getRecommendedVenuePriceCategory()
            v_rating = sights[0].getRecommendedVenueRating()
            message = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' + v_address +  '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)

        dispatcher.utter_message(prepareResponseJson(self.name(), message, tracker))
        return []

class ActionSuggestWeather(Action):
    def name(self):
        return 'action_suggest_weather'

    def run(self, dispatcher, tracker, domain):
        # get the location entity from the console
        location = tracker.get_slot('location')
        date = tracker.get_slot('time')
        # init the weather Client
        weatherClient = YahooClient()
        # fetch the weather data
        weather = weatherClient.fetch_weather_for_city(str(location))

        data = {}
        data['action_name'] = self.name()
        message = 'No data could be found.'


        if str(date) == "None":
            # get the weather factors
            description = weather.getWeatherDescription()
            condition = weather.getWeatherConditionFactors()
            conditionDesc = condition.getConditionDescription()
            conditionTemp = condition.getConditionCurrentTemperature()
            conditionDate = condition.getLastUpdatedConditionDate()

            message = description + '\nCondition: ' + conditionDesc + '\nThe currrent temperature is ' + conditionTemp + ' degree\nLast updated ' + conditionDate
        else:
            date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
            for num in range(0, len(weather.getWeatherForecastFactors())):
                forecast = weather.getWeatherForecastFactors()[num]
                if date.strftime('%d %b %Y') == forecast.getLastUpdatedForecastDate():
                    # get the weather factors
                    description = weather.getWeatherDescription()
                    forecastDesc = forecast.getForecastDescription()
                    forecastHigh = forecast.getForecastHighTemperature()
                    forecastLow = forecast.getForecastLowTemperature()
                    forecastDate = forecast.getLastUpdatedForecastDate()

                    message = description + ' on ' + forecastDate + '\nCondition: ' + forecastDesc + '\nThe temperature is between ' + forecastLow + ' and ' + forecastHigh + ' degree'

        dispatcher.utter_message(prepareResponseJson(self.name(), message, tracker))
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
        message = "I couldn't find more sights"
        # get the venue factors
        global sightsCounter
        if sights is not None and len(sights) > sightsCounter + 1:
            sightsCounter = sightsCounter + 1
            v_name = sights[0].getRecommendedVenueName()
            v_contact = sights[0].getRecommendedVenueContact()
            v_address = sights[0].getRecommendedVenueAddress()
            v_price = sights[0].getRecommendedVenuePriceCategory()
            v_rating = sights[0].getRecommendedVenueRating()
            message = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' + v_address + '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)

        dispatcher.utter_message(prepareResponseJson(self.name(), message, tracker))
        return []

class ActionFindAlternativeSight(Action):
    def name(self):
        return 'action_find_alternative_sight'

    def run(self, dispatcher, tracker, domain):
        message = "I couldn't find more restaurants"
        # get the venue factors
        global restaurantsCounter
        if restaurants is not None and len(restaurants) > restaurantsCounter + 1:
            restaurantsCounter = restaurantsCounter + 1
            v_name = restaurants[restaurantsCounter].getRecommendedVenueName()
            v_contact = restaurants[restaurantsCounter].getRecommendedVenueContact()
            v_address = restaurants[restaurantsCounter].getRecommendedVenueAddress()
            v_price = restaurants[restaurantsCounter].getRecommendedVenuePriceCategory()
            v_rating = restaurants[restaurantsCounter].getRecommendedVenueRating()
            message = v_name +  '\nContact: ' + v_contact +  '\nAddress: ' + v_address + '\nPrice Category: ' + v_price +  '\nRating: ' + str(v_rating)

        dispatcher.utter_message(prepareResponseJson(self.name(), message, tracker))
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
