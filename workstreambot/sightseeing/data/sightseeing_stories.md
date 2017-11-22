<!-- LOCATION given -->

## story_sightseeing_1
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _deny[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_2
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _deny[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_3
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=closing_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

  ## story_sightseeing_4
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=closing_time]
 - action_suggest
* _request_info[info=opening_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

   ## story_sightseeing_5
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=closing_time]
 - action_suggest
* _request_info[info=opening_time]
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

  ## story_sightseeing_6
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=rating]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

  ## story_sightseeing_7
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=opening_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

   ## story_sightseeing_8
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _request_info[info=opening_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

    ## story_sightseeing_9
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[location=berlin]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye




<!-- TYPE SPECIFIC given -->

 ## story_sightseeing_10
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _deny[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_11
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _deny[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_12
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _deny[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_13
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=opening_time]
 - action_suggest
* _request_info[info=closing_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_14
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

  ## story_sightseeing_15
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _deny[]
 - utter_yourewelcomed
 - utter_goodbye

  ## story_sightseeing_16
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=rating]
 - action_suggest
* _request_info[info=closing_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_17
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _request_info[info=opening_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

  ## story_sightseeing_18
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type_specific=museum]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _request_info[info=opening_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye



<!-- TYPE given -->

 ## story_sightseeing_19
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=indoors]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=rating]
 - action_suggest
* _request_info[info=closing_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_20
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=outdoors]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _request_info[info=closing_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_21
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=indoors]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _deny[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_22
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=outdoors]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=phone_num]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_23
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=outdoors]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=expensive]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _request_info[info=opening_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_24
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=outdoors]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_25
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=outdoors]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=phone_num]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_26
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=indoors]
 - utter_ask_location
* _inform[location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=rating]
 - action_suggest
* _request_info[info=closing_time]
 - action_suggest
* _request_info[info=opening_time]
 - action_suggest
* _request_info[info=phone_num]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye



<!-- TYPE & LOCATION given -->

 ## story_sightseeing_27
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=indoors, location=berlin]
 - utter_ask_price
* _inform[price=expensive]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=closing_time]
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_28
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=indoors, location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _request_info[info=closing_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_29
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=indoors, location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _deny[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_30
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=indoors, location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=phone_num]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_31
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=outdoors, location=berlin]
 - utter_ask_price
* _inform[price=expensive]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _request_info[info=opening_time]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_32
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=outdoors, location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_33
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=indoors, location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _deny[]
 - utter_ack_findalternatives
 - action_search_restaurants
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=phone_num]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye

 ## story_sightseeing_34
* _greet[]
 - utter_greet
 - utter_ask_howcanhelp
* _inform[type=outdoors, location=berlin]
 - utter_ask_price
* _inform[price=cheap]
 - utter_ack_dosearch
 - action_searchsights
 - action_suggest
* _affirm[]
 - utter_ask_helpmore
* _request_info[info=opening_time]
 - action_suggest
* _request_info[info=closing_time]
 - action_suggest
* _request_info[info=rating]
 - action_suggest
* _request_info[info=phone_num]
 - action_suggest
* _thankyou[]
 - utter_yourewelcomed
 - utter_goodbye