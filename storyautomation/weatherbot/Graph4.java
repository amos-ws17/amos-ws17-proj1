package amos.sprint8;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Graph4 {
	
	private int numOfVertices = 0;
	private Map<String, List<String>> adjLists = null;
	
	public Graph4(List<String> actions) {
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
		Map<String, Boolean> vis = new HashMap<>(numOfVertices);
		for(String s : adjLists.keySet()) {
			vis.put(s, false);
		}
		boolean[] visited = new boolean[numOfVertices];

		// Create an array to store paths
		Map<Integer, String> p = new HashMap<>(numOfVertices);
		int[] path = new int[numOfVertices];
		int pathIndex = 0; // Initialize path[] as empty

		// Initialize all vertices as not visited
		for (int i = 0; i < numOfVertices; i++) {
			visited[i] = false;
		}

		// Call the recursive helper function to print all paths
		printAllPathsUtil(from, to, vis, p, pathIndex);
	}
	
	private void printAllPathsUtil(String from, String to, Map<String, Boolean> visited,
			Map<Integer, String> path, int pathIndex) {
		visited.put(from, true);
		path.put(pathIndex, from);
		pathIndex++;
		
		if(from.equalsIgnoreCase(to)) {
			PrintWriter pw = null;
			try {
				pw = new PrintWriter(new FileWriter("weather_stories.md", true));
				String[] cities = {"Berlin", "Paris", "Sofia", "Madrid", "Rome"};
				String[] dates = {"yesterday","today", "tomorrow", "2017-12-12", "2017-12-13", "2017-12-14"};
				
//				System.out.println("## New story");
				StringBuilder sb = new StringBuilder();
				for(int i = 0; i < pathIndex; i++) {
					if(path.get(i).startsWith("_")) {
						sb.append("* " + path.get(i) + System.lineSeparator());
//							System.out.println("* " + path.get(i));
					} else {
						sb.append("  - " + path.get(i) + System.lineSeparator());
//							System.out.println("  - " + path.get(i));	
					}
				}
				sb.append(System.lineSeparator());
				String template = sb.toString();
				for(String city : cities) {
					for(String date : dates) {
						int startIndex = sb.indexOf("_inform[location,date]");
						sb.replace(startIndex, startIndex + 22, 
								"_inform[location=" + city + ",date=" + date +"]");
//						System.out.println(sb);
						pw.write(sb.toString());
						sb = new StringBuilder(template);
					}
				}
//					System.out.println(sb);
//					System.out.println();
			} catch(IOException e) {
				e.printStackTrace();
			} finally {
				pw.close();
			}
		} else {
			for(String s : adjLists.get(from)) {
				if(!visited.get(s))
					printAllPathsUtil(s, to, visited, path, pathIndex);	
			}
		}
		
		// Remove current vertex from path[] and mark it as unvisited
		pathIndex--;
		visited.put(from, false);
	}
	
	private class Vertex<T> {
		
		private T value = null;
		
		public Vertex(T value) {
			this.value = value;
		}
	}
}
