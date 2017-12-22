## weather
* _switch_weather[]
  - utter_ask_location
* _inform[location=berlin]
  - action_search_weather

## weather at time
* _switch_weather[time=2017-01-01]
  - utter_ask_location
* _inform[location=berlin]
  - action_search_weather

## weather in location
* _switch_weather[location=berlin]
  - action_search_weather

## weather in location at time
* _switch_weather[location=berlin,time=2017-01-01]
  - action_search_weather