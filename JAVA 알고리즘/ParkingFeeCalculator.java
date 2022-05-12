package solution;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class ParkingFeeCalculator {
	public static int defaultTime = 0;
	public static int defaultFee = 0;
	public static int unitTime = 0;
	public static int unitFee = 0;
	public static Map<String, Integer> park = new TreeMap(); // TreeMap : Key를 기준으로 정렬
	public static Map<String, Integer> CumulativeTimes = new TreeMap();
	
	public static void main(String[] args) {
		int[] fees = {180, 5000, 10, 600};
		String[] records = {"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"};
		
		solution(fees, records);
	}
	
	public static int[] solution(int[] fees, String[] records) {
        setFee(fees);
        readRecodes(records);
        calculateTimeByRemainCars();
        
        int[] answer = new int[CumulativeTimes.size()]; 
        int count = 0;
        for (String key: CumulativeTimes.keySet()){  
			answer[count] = calulateFee(CumulativeTimes.get(key));
			count++;
		} 
        
        return answer;
    }
	
	public static void setFee(int[] fees) {
		defaultTime = fees[0];
		defaultFee = fees[1];
		unitTime = fees[2];
		unitFee = fees[3];
        return;
    }
	
	public static void readRecodes(String[] records) {
		for(int i = 0 ; i < records.length; i++) {
			settlingFees(records[i]);        	
        }
        return;
    }
	
	public static void settlingFees(String record) {
		String[] info = record.split(" ");
		String car = info[1];
		int time = timeToMinutes(info[0]);
		String type = info[2];
		
		if(type.equals("IN")) {
			if(!isFirstVisit(car)) {
				park.put(car, time);
				CumulativeTimes.put(car, 0);
				
			}else {
				park.put(car, time);
				
			}
			
		}else if(type.equals("OUT") && isParking(car)) {
			int inTime = (int) park.remove(car); 			// map.remove(key) : map에서 제거하면서 value 반환
			int outTime = time;
			int plusTime = outTime - inTime;
			int cumulativeTime = (int) CumulativeTimes.get(car);
			
			CumulativeTimes.put(car, cumulativeTime+plusTime);
		}
		
        return;
    }
	
	public static int timeToMinutes(String formatTime) {
		int totalMinutes = 0;
		String hour = ""+ formatTime.charAt(0) + formatTime.charAt(1);
		String minutes = ""+ formatTime.charAt(3) + formatTime.charAt(4);
		
		totalMinutes = Integer.parseInt(hour) * 60 + Integer.parseInt(minutes);
        return totalMinutes;
    }
	
	public static void calculateTimeByRemainCars() {
		for (String car: park.keySet()){  
        	settlingFeesByRemainCar(car);
		}
        return;
    }
	
	// * keySet을 하면서 remove를 하면 동시성 오류가 발생하므로 remove -> get으로 변경
	public static void settlingFeesByRemainCar(String car) {
		int inTime = (int) park.get(car);
		int outTime = 23*60 + 59; // 23:59
		int plusTime = outTime - inTime;
		int cumulativeTime = (int) CumulativeTimes.get(car);
		
		CumulativeTimes.put(car, cumulativeTime+plusTime);
        return;
    }
	
	public static boolean isParking(String car) {
        return park.containsKey(car)?true:false;
    }
	
	public static boolean isFirstVisit(String car) {
        return CumulativeTimes.containsKey(car)?true:false;
    }
	
	public static int calulateFee(int minutes) {
		double extraTime;
		double extraUnit;
		
		if(minutes <= defaultTime) 
			return defaultFee;
		else {
			extraTime = minutes >= defaultTime ? minutes-defaultTime : defaultTime-minutes;
//			extraUnit = extraTime >= unitTime ? Math.ceil(extraTime/unitTime):1;
			extraUnit = Math.ceil(extraTime/unitTime);
			return (int) (defaultFee + extraUnit*unitFee);
		} 
	}
}
