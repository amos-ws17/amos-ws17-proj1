package amos.storyautomation.weather;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Starter {
	public static void main(String[] args) {
		
		List<String> weatherActions = new ArrayList<>();
		weatherActions.add("_greet[]");
		weatherActions.add("utter_greet");
		weatherActions.add("utter_ask_howcanhelp");
		weatherActions.add("_inform[location,time]");
		weatherActions.add("utter_on_it");
		weatherActions.add("utter_ask_location");
		weatherActions.add("_inform[location]");
		weatherActions.add("utter_ack_dosearch");
		weatherActions.add("action_search_weather");
		weatherActions.add("utter_ask_helpmore");
		weatherActions.add("_goodbye[]");
		weatherActions.add("utter_goodbye");
		
		GraphWeather flowChart = new GraphWeather(weatherActions);

		flowChart.addEdge("_greet[]", "utter_greet");
		flowChart.addEdge("utter_greet", "utter_ask_howcanhelp");
		flowChart.addEdge("utter_ask_howcanhelp", "_inform[location,time]");
		flowChart.addEdge("_inform[location,time]", "utter_on_it");
		flowChart.addEdge("utter_on_it", "utter_ask_location");
		flowChart.addEdge("utter_on_it", "utter_ack_dosearch");
		flowChart.addEdge("utter_ask_location", "_inform[location]");
		flowChart.addEdge("_inform[location]", "utter_ack_dosearch");
		flowChart.addEdge("utter_ack_dosearch", "action_search_weather");
		flowChart.addEdge("action_search_weather", "utter_ask_helpmore");
		flowChart.addEdge("utter_ask_helpmore", "_goodbye[]");
		flowChart.addEdge("utter_ask_helpmore", "_inform[location,time]");
		flowChart.addEdge("_goodbye[]", "utter_goodbye");
		
		String start = weatherActions.get(0), end = weatherActions.get(weatherActions.size() - 1);
//		System.out.println("Following are all different paths from " + start + " to " + end);
		flowChart.printAllPaths(start, end);
	}
}
