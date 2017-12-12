package amos.storyautomation.weather;

public class DateGenerator {
	
	public static String generateDatesForYear(int year) {
		StringBuilder dates = new StringBuilder();
		int month = 0;
		int day = 0;
		int[] months = {1,3,5,7,9,11};
		for(int m : months) {
			for(int d = 1; d < 32; d++) {
				if(m < 10 && d < 10)
					dates.append(year + "-0" + m + "-0" + d + ',');
				else if(m < 10 && d > 9)
					dates.append(year + "-0" + m + "-" + d + ',');
				else if(m > 9 && d > 9)
					dates.append(year + "-" + m + "-" + d + ',');
			}
		}
		dates.append("yesterday,today,tomorrow");
		return dates.toString();
	}
}
