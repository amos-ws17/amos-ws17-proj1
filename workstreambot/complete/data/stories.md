## greet
* _greet
  - utter_greet
  - utter_ask_how_can_help
> check_asked_how_can_help

## inform sights
> check_asked_how_can_help
* _inform_sightseeing[]
> check_ask_location_sights

## inform sights type_specific
> check_asked_how_can_help
* _inform_sightseeing[type_specific=museum]
> check_ask_location_sights

## inform sights location
> check_asked_how_can_help
* _inform_sightseeing[location=berlin]
> check_do_search_sights

## inform sights location and type_specific
> check_asked_how_can_help
* _inform_sightseeing[location=berlin,type_specific=museum]
> check_do_search_sights

## inform sights type
> check_asked_how_can_help
* _inform_sightseeing[type=indoor]
  - utter_ask_location
* _inform[location=berlin]
> check_ask_price_sights

## inform sights type and location
> check_asked_how_can_help
* _inform_sightseeing[type=indoor,location=berlin]
> check_ask_price_sights

## ask location (sights)
> check_ask_location_sights
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_sights

## ask price (sights)
> check_ask_price_sights
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_sights

## do search sights
> check_do_search_sights
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
> check_asked_like_it_sights

## affirm like it (sights)
> check_asked_like_it_sights
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more

## deny like it (sights)
> check_asked_like_it_sights
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more

## inform weather location
> check_asked_how_can_help
* _inform_weather[location=berlin]
> check_do_search_weather

## inform weather location and time
> check_asked_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
> check_do_search_weather

## inform weather time
> check_asked_how_can_help
* _inform_weather[time=2018-01-01]
> check_ask_location_weather

## inform weather
> check_ask_how_can_help
* _inform_weather[]
> check_ask_location_weather

## asked location (weather)
> check_ask_location_weather
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_weather

## do search weather
> check_do_search_weather
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
> check_asked_help_more

## inform restaurant location, cuisine and price
> check_asked_how_can_help
* _inform_restaurant[location=berlin,cuisine=italian,price=cheap]
> check_do_search_restaurant

## inform restaurant location and price
> check_asked_how_can_help
* _inform_restaurant[location=berlin,price=cheap]
  - utter_ask_cuisine
* _inform[cuisine=italian]
> check_do_search_restaurant

## inform restaurant location and cuisine
> check_asked_how_can_help
* _inform_restaurant[location=berlin,cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant

## inform restaurant location
> check_asked_how_can_help
* _inform_restaurant[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant

## inform restaurant cuisine and price
> check_asked_how_can_help
* _inform_restaurant[cuisine=italian,price=cheap]
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_restaurant

## inform restaurant cuisine
> check_asked_how_can_help
* _inform_restaurant[cuisine=italian]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant

## inform restaurant price
> check_asked_how_can_help
* _inform_restaurant[price=cheap]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
> check_do_search_restaurant

## do search restaurant
> check_do_search_restaurant
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
> check_asked_like_it_restaurant

## affirm like it (restaurant)
> check_asked_like_it_restaurant
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more

## deny like it (restaurant)
> check_asked_like_it_restaurant
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more

## affirm help more
> check_asked_help_more
* _affirm[]
  - utter_ask_how_can_help

## deny help more
> check_asked_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye
