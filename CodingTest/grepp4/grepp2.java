package test;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class grepp2 {
	public static void main(String[] args) {
		String[] grades = {"DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+", "DS7651 A+", "OS1808 B-"};
		solution(grades);
	}
	public static String[] solution(String[] grades) {
		int gradesSize = grades.length;
		String[] aphb = {"A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D+", "D0", "D-", "F"};
		
		HashMap result = new HashMap();
		
		for(int i = 0; i < gradesSize; i++) {
			String[] detail = grades[i].split(" ");
			String coures = detail[0];
			String score = detail[1];
			
			if(!result.containsKey(coures)) {
				result.put(coures, score);
			} else {
				System.out.println("여기");
				int in = Arrays.asList(aphb).indexOf(result.get(coures));
				int input = Arrays.asList(aphb).indexOf(score);
				if(in > input) {
					result.put(coures, score);
					//System.out.println(coures+" "+score);
					//System.out.println(Arrays.asList(result));
				}
			}
		}
		
		List<Map.Entry<String, Integer>> entryList = new LinkedList<>(result.entrySet());
		entryList.sort(new Comparator<Map.Entry<String, Integer>>() {
		    @Override
		    public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
			return Arrays.asList(aphb).indexOf(o1.getValue()) - Arrays.asList(aphb).indexOf(o2.getValue());
		    }
		});
		String[] answer = new String[entryList.size()];
		int index = 0;
		for(Map.Entry<String, Integer> entry : entryList){
			String saveStr= entry.getKey()+" "+entry.getValue();
			answer[index] = saveStr;
			index++;
			System.out.println(saveStr);
		}
		


		System.out.println(Arrays.asList(result));

		
        return answer;
    }
}
