## one time simple path 1              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## one time simple path 2             <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform[date=1january]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## one time path with extension 1            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform[date=1january]
  - utter_on_it
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## multiple time simple path 1              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform[date=1january]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
*_inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time simple path 2              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
*_inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## multiple time simple path 3              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
*_inform[date=1january]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time simple path 4              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform[date=1january]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
*_inform[date=1january]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye  
  
## multiple time path with extension 1            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform[date=1january]
  - utter_on_it
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 2            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform[date=1january]
  - utter_on_it
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _inform[date=1january]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 3            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform[date=1january]
  - utter_on_it
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _inform[date=1january]
  - utter_on_it
  - utter_ask_location
* _inform[location=berlin]
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
