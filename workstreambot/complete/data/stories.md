## greet
* _greet
  - utter_greet
  - utter_ask_how_can_help
> check_asked_how_can_help_1

## inform sights
> check_asked_how_can_help_1
* _inform_sightseeing[]
> check_ask_location_sights_1

## inform sights type_specific
> check_asked_how_can_help_1
* _inform_sightseeing[type_specific=museum]
> check_ask_location_sights_1

## inform sights location
> check_asked_how_can_help_1
* _inform_sightseeing[location=berlin]
> check_do_search_sights_1

## inform sights location and type_specific
> check_asked_how_can_help_1
* _inform_sightseeing[location=berlin,type_specific=museum]
> check_do_search_sights_1

## inform sights type
> check_asked_how_can_help_1
* _inform_sightseeing[type=indoor]
  - utter_ask_location
* _inform[location=berlin]
> check_ask_price_sights_1

## inform sights type and location
> check_asked_how_can_help_1
* _inform_sightseeing[type=indoor,location=berlin]
> check_ask_price_sights_1

## ask location (sights)
> check_ask_location_sights_1
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_sights_1

## ask price (sights)
> check_ask_price_sights_1
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_sights_1

## do search sights
> check_do_search_sights_1
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
> check_asked_like_it_sights_1

## affirm like it (sights)
> check_asked_like_it_sights_1
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more_1

## deny like it (sights)
> check_asked_like_it_sights_1
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more_1

## inform weather location
> check_asked_how_can_help_1
* _inform_weather[location=berlin]
> check_do_search_weather_1

## inform weather location and time
> check_asked_how_can_help_1
* _inform_weather[location=berlin,time=2018-01-01]
> check_do_search_weather_1

## inform weather time
> check_asked_how_can_help_1
* _inform_weather[time=2018-01-01]
> check_ask_location_weather_1

## inform weather
> check_ask_how_can_help_1
* _inform_weather[]
> check_ask_location_weather_1

## asked location (weather)
> check_ask_location_weather_1
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_weather_1

## do search weather
> check_do_search_weather_1
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
> check_asked_help_more_1

## inform restaurant location, cuisine and price
> check_asked_how_can_help_1
* _inform_restaurant[location=berlin,cuisine=italian,price=cheap]
> check_do_search_restaurant_1

## inform restaurant location and price
> check_asked_how_can_help_1
* _inform_restaurant[location=berlin,price=cheap]
  - utter_ask_cuisine
* _inform[cuisine=italian]
> check_do_search_restaurant_1

## inform restaurant location and cuisine
> check_asked_how_can_help_1
* _inform_restaurant[location=berlin,cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant_1

## inform restaurant location
> check_asked_how_can_help_1
* _inform_restaurant[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant_1

## inform restaurant cuisine and price
> check_asked_how_can_help_1
* _inform_restaurant[cuisine=italian,price=cheap]
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_restaurant_1

## inform restaurant cuisine
> check_asked_how_can_help_1
* _inform_restaurant[cuisine=italian]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant_1

## inform restaurant price
> check_asked_how_can_help_1
* _inform_restaurant[price=cheap]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
> check_do_search_restaurant_1

## do search restaurant
> check_do_search_restaurant_1
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
> check_asked_like_it_restaurant_1

## affirm like it (restaurant)
> check_asked_like_it_restaurant_1
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more_1

## deny like it (restaurant)
> check_asked_like_it_restaurant_1
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more_1

## affirm help more
> check_asked_help_more_1
* _affirm[]
> check_start_conversation_2

## deny help more
> check_asked_help_more_1
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye



## start conversation
> check_start_conversation_2
  - utter_ask_how_can_help
> check_asked_how_can_help_2

## inform sights
> check_asked_how_can_help_2
* _inform_sightseeing[]
> check_ask_location_sights_2

## inform sights type_specific
> check_asked_how_can_help_2
* _inform_sightseeing[type_specific=museum]
> check_ask_location_sights_2

## inform sights location
> check_asked_how_can_help_2
* _inform_sightseeing[location=berlin]
> check_do_search_sights_2

## inform sights location and type_specific
> check_asked_how_can_help_2
* _inform_sightseeing[location=berlin,type_specific=museum]
> check_do_search_sights_2

## inform sights type
> check_asked_how_can_help_2
* _inform_sightseeing[type=indoor]
  - utter_ask_location
* _inform[location=berlin]
> check_ask_price_sights_2

## inform sights type and location
> check_asked_how_can_help_2
* _inform_sightseeing[type=indoor,location=berlin]
> check_ask_price_sights_2

## ask location (sights)
> check_ask_location_sights_2
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_sights_2

## ask price (sights)
> check_ask_price_sights_2
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_sights_2

## do search sights
> check_do_search_sights_2
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
> check_asked_like_it_sights_2

## affirm like it (sights)
> check_asked_like_it_sights_2
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more_2

## deny like it (sights)
> check_asked_like_it_sights_2
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more_2

## inform weather location
> check_asked_how_can_help_2
* _inform_weather[location=berlin]
> check_do_search_weather_2

## inform weather location and time
> check_asked_how_can_help_2
* _inform_weather[location=berlin,time=2018-01-01]
> check_do_search_weather_2

## inform weather time
> check_asked_how_can_help_2
* _inform_weather[time=2018-01-01]
> check_ask_location_weather_2

## inform weather
> check_ask_how_can_help_2
* _inform_weather[]
> check_ask_location_weather_2

## asked location (weather)
> check_ask_location_weather_2
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_weather_2

## do search weather
> check_do_search_weather_2
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
> check_asked_help_more_2

## inform restaurant location, cuisine and price
> check_asked_how_can_help_2
* _inform_restaurant[location=berlin,cuisine=italian,price=cheap]
> check_do_search_restaurant_2

## inform restaurant location and price
> check_asked_how_can_help_2
* _inform_restaurant[location=berlin,price=cheap]
  - utter_ask_cuisine
* _inform[cuisine=italian]
> check_do_search_restaurant_2

## inform restaurant location and cuisine
> check_asked_how_can_help_2
* _inform_restaurant[location=berlin,cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant_2

## inform restaurant location
> check_asked_how_can_help_2
* _inform_restaurant[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant_2

## inform restaurant cuisine and price
> check_asked_how_can_help_2
* _inform_restaurant[cuisine=italian,price=cheap]
  - utter_ask_location
* _inform[location=berlin]
> check_do_search_restaurant_2

## inform restaurant cuisine
> check_asked_how_can_help_2
* _inform_restaurant[cuisine=italian]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_price
* _inform[price=cheap]
> check_do_search_restaurant_2

## inform restaurant price
> check_asked_how_can_help_2
* _inform_restaurant[price=cheap]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
> check_do_search_restaurant_2

## do search restaurant
> check_do_search_restaurant_2
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
> check_asked_like_it_restaurant_2

## affirm like it (restaurant)
> check_asked_like_it_restaurant_2
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more_2

## deny like it (restaurant)
> check_asked_like_it_restaurant_2
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
> check_asked_help_more_2

## affirm help more
> check_asked_help_more_2
* _affirm[]

## deny help more
> check_asked_help_more_2
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye
