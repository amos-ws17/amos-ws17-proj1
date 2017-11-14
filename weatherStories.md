## one time simple path 1              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform_date
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## one time simple path 2             <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform_location
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## one time path with extension 1            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_location
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## one time path with extension 2            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_date
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## multiple time simple path 1              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform_date
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
*_inform_location
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time simple path 2              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform_location
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
*_inform_location
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye

## multiple time simple path 3              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform_location
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
*_inform_date
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time simple path 4              <!-- name of the story - just for debugging -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp
* _inform_date
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
*_inform_date
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye  
  
## multiple time path with extension 1            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_location
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _inform_location
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 2            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_date
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _inform_location
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 3            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_date
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _inform_date
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 4            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_location
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _inform_date
  - utter_on_it
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 5            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_location
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _inform_date
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 6            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_date
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _inform_location
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 7            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_location
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _inform_location
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
  
## multiple time path with extension 8            <!-- this is already the start of the next story -->
* _greet              
  - utter_greet
  - utter_ask_howcanhelp           			 <!-- action of the bot to execute -->
* _inform_date
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _inform_date
  - utter_on_it
  - utter_ask_location
* _inform_location
  - utter_ack_dosearch
  - bot.ActionSearchWeather
  - utter_ask_helpmore
* _thankyou
  - utter_goodbye
