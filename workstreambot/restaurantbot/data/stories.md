## simple path 1
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=cheap]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye

## simple path 2
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=expensive]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye
  
## simple path 3
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye

## simple path 4
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=cheap]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _deny 
  - utter_yourewelcomed
  - utter_goodbye

## simple path 5
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=expensive]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _deny 
  - utter_yourewelcomed
  - utter_goodbye

## simple path 6
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _deny 
  - utter_yourewelcomed
  - utter_goodbye

## complex path 1
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye
 
## complex path 2
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=expensive]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye

## complex path 3
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=cheap]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye

## complex path 4
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=cheap]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=cheap]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye

## complex path 5
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=cheap]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=expensive]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye

## complex path 6
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=cheap]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye
  
## complex path 7
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=expensive]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye

## complex path 8
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=expensive]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=cheap]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye
  
## complex path 9
* _greet
  - utter_greet
  - utter_ask_location
* _inform[location=berlin]
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=expensive]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _deny
  - utter_ask_helpmore
* _affirm
  - utter_ask_cuisine
* _inform[cuisine=mexican,price=expensive]
  - utter_on_it
  - utter_ack_dosearch
  - utter_suggest
* _affirm
  - utter_yourewelcomed
  - utter_goodbye