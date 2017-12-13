package amos.storyautomation.weather;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.concurrent.ThreadLocalRandom;

public class GraphWeather {
	
	private int numOfVertices = 0;
	private Map<String, List<String>> adjLists = null;
	private int stories = 0;
	private static final int CYCLES = 10;
	private int counter = 0;
	
	public GraphWeather(List<String> actions) {
		this.numOfVertices = actions.size();
		adjLists = new HashMap<String, List<String>>(numOfVertices);
		for(int i = 0; i < numOfVertices; i++) {
			adjLists.put(actions.get(i), new ArrayList<String>());
		}
	}
	
	public int getAdjListsSize() {
		return adjLists.size();
	}
	
	public void addEdge(String from, String to) {
		adjLists.get(from).add(to);
	}
	
	public void printAllPaths(String from, String to) {
		Map<String, Boolean> visited = new HashMap<>(numOfVertices);
		for(String s : adjLists.keySet()) {
			visited.put(s, false);
		}

		// Create an array to store paths
		Map<Integer, String> path = new HashMap<>(numOfVertices);
		int pathIndex = 0; // Initialize path[] as empty

		// Call the recursive helper function to print all paths
		printAllPathsUtil(from, to, visited, path, pathIndex);
	}
	
	private void printAllPathsUtil(String from, String to, Map<String, Boolean> visited,
			Map<Integer, String> path, int pathIndex) {
		
		visited.put(from, true);
		path.put(pathIndex, from);
		pathIndex++;
		
		if(from.equalsIgnoreCase(to)) {
			String[] cities = {"Berlin", "Paris", "Sofia", "Madrid", "Rome",
					"Helsinki", "Oslo", "London", "Prague", "Budapest", "Amsterdam",
					"New York", "San Francisco", "Los Angeles", "Las Vegas", "Boston"};
			String[] dates = DateGenerator.generateDatesForYear(2017).split(",");
			generateStories(cities, dates, pathIndex, path);
		} else {
			for(String s : adjLists.get(from)) {
				if(!visited.get(s))
					printAllPathsUtil(s, to, visited, path, pathIndex);
				else {
					counter++;
					if(counter <= CYCLES)
						printAllPathsUtil(s, to, visited, path, pathIndex);
				}
			}
		}
		
		// Remove current vertex from path[] and mark it as unvisited
		pathIndex--;
		visited.put(from, false);
	}
	
	private void generateStories(String[] cities, String[] dates, int pathIndex, Map<Integer, String> path) {

		PrintWriter pw = null;
		try {
			pw = new PrintWriter(new FileWriter("weather_stories.md", true));
			StringBuilder sb = new StringBuilder();
			for(int i = 0; i < pathIndex; i++) {
				if(path.get(i).startsWith("_")) {
					sb.append("* " + path.get(i) + System.lineSeparator());
				} else {
					sb.append("  - " + path.get(i) + System.lineSeparator());
				}
			}
			
			final String template = sb.toString();
			System.out.println(template);
			if(template.contains("_inform[location,time]") && 
					template.contains("_inform[location]")) {
				for(String city : cities) {
					for(String date : dates) {
						String story = "## Story " + stories + "\n";
						story += template;
						stories++;
						story = story.replace("_inform[location,time]",
								"_inform[location=" + city + ",time=" + date +"]");
						int randomNum = ThreadLocalRandom.current().nextInt(0, cities.length);
						story = story.replace("_inform[location]", 
								"_inform[location=" + cities[randomNum] + "]");
						pw.write(story + "\n");
					}
				}
			} else if(template.contains("_inform[location,time]")) {
				for(String city : cities) {
					for(String date : dates) {
						String story = "## Story " + stories + "\n";
						story += template;
						stories++;
						story = story.replace("_inform[location,time]",
								"_inform[location=" + city + ",time=" + date +"]");
						pw.write(story + "\n");
					}
				}
			} else if(template.contains("_inform[location]")) {
				for(String city : cities) {
					for(String date : dates) {
						String story = "## Story " + stories + "\n";
						story += template;
						stories++;
						int randomNum = ThreadLocalRandom.current().nextInt(0, cities.length);
						story = story.replace("_inform[location]", 
								"_inform[location=" + cities[randomNum] + "]");
						pw.write(story + "\n");
					}
				}
			}
		} catch(IOException e) {
			e.printStackTrace();
		} finally {
			pw.close();
		}
	}
}

