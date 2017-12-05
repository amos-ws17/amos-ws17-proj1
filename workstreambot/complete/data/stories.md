## inform weather
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform weather
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform weather time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform weather location/time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform weather location
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform restaurant like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_restaurant[]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform restaurant don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_restaurant[]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform restaurant location like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform restaurant location don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform restaurant price like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
_inform_restaurant[price=cheap]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform restaurant price don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
_inform_restaurant[price=cheap]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform restaurant cuisine like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_restaurant[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather + inform restaurant cuisine don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_restaurant[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather time + inform weather
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather time + inform weather time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather time + inform weather location/time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather time + inform weather location
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location/time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location/time + inform weather
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location/time + inform weather time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location/time + inform weather location/time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location/time + inform weather location
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location + inform weather
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location + inform weather time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location + inform weather location/time
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[location=berlin,time=2018-01-01]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform weather location + inform weather location
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _affirm[]
  - utter_ask_how_can_help
* _inform_weather[location=berlin]
  - utter_ack_do_search
  - action_suggest_weather
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant location like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant location don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant price like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[price=cheap]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant price don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[price=cheap]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant cuisine like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[cuisine=italian]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant cuisine don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[cuisine=italian]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant location/price like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin,price=cheap]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant location/price don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin,price=cheap]
  - utter_ask_cuisine
* _inform[cuisine=italian]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant location/cuisine like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin,cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant location/cuisine don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin,cuisine=italian]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant cuisine/price like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[cuisine=italian,price=cheap]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant cuisine/price don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[cuisine=italian,price=cheap]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant location/cuisine/price like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin,cuisine=italian,price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform restaurant location/cuisine/price don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_restaurant[location=berlin,cuisine=italian,price=cheap]
  - utter_ack_do_search
  - action_suggest_restaurant
  - utter_like_it
* _deny[]
  - action_find_alternative_restaurant
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing type_specific like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[type_specific=museum]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing type_specific don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[type_specific=museum]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing location like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[location=berlin]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing location don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[location=berlin]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing type like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[type=indoor]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing type don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[type=indoor]
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing location/type_specific like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[location=berlin,type_specific=museum]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing location/type_specific don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[location=berlin,type_specific=museum]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing location/type like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[location=berlin,type=indoor]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye

## inform sightseeing location/type don't like it
* _greet
  - utter_greet
  - utter_ask_how_can_help
* _inform_sightseeing[location=berlin,type=indoor]
  - utter_ask_price
* _inform[price=cheap]
  - utter_ack_do_search
  - action_suggest_sights
  - utter_like_it
* _deny[]
  - action_find_alternative_sight
  - utter_like_it
* _affirm[]
  - utter_ask_help_more
* _deny[]
  - utter_youre_welcomed
  - utter_goodbye
