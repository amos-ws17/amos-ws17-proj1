## weather in location path
* _greet
  - utter_greet
  - utter_ask_howcanhelp
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _goodbye
  - utter_goodbye

## weather in location for date path
* _greet
  - utter_greet
  - utter_ask_howcanhelp
* _inform[location=berlin,date=01-01-2017]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _goodbye
  - utter_goodbye

## ask for location path 1
* _greet
  - utter_greet
  - utter_ask_howcanhelp
* _inform[]
  - utter_on_it
  - utter_ask_location
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _goodbye
  - utter_goodbye

## ask for location path 2
* _greet
  - utter_greet
  - utter_ask_howcanhelp
* _inform[date=01-01-2017]
  - utter_on_it
  - utter_ask_location
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _goodbye
  - utter_goodbye
  
## remember location path
* _greet
  - utter_greet
  - utter_ask_howcanhelp
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _inform[date=01-01-2017]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _goodbye
  - utter_goodbye

## override location path
* _greet
  - utter_greet
  - utter_ask_howcanhelp
* _inform[location=berlin]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _inform[location=new york]
  - utter_on_it
  - utter_ack_dosearch
  - action_search_weather
  - utter_ask_helpmore
* _goodbye
  - utter_goodbye
