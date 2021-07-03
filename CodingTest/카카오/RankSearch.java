package test;

import java.util.ArrayList;
import java.util.HashMap;

public class RankSearch {
	public static void main(String[] args) {
		String[] info = {"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"};
		String[] query = {"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"};
		solution(info, query);
	}
	
	public static int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        ArrayList<HashMap<String, String>> list = new ArrayList<>();
        ArrayList<String[]> list2 = new ArrayList<>();
        
        for(int i = 0; i < info.length; i++) {
        	HashMap<String,String> map1 = new HashMap<String,String>();
        	String[] some = info[i].split(" ");
        	map1.put("lan", some[0]);
        	map1.put("group", some[1]);
        	map1.put("career", some[2]);
        	map1.put("food", some[3]);
        	map1.put("score", some[4]);
        	list.add(map1);
        }
        
        for(int i = 0; i < query.length; i++) {
        	list2.add(query[i].replaceAll(" and", "").split(" "));
        }
        
        for(int j = 0; j < query.length; j++) {
        	String[] quertList = list2.get(j);
        	int count = 0;
        	for(int i = 0; i < list.size(); i++) {
        		if (check(list.get(i), quertList)) {
        			count++;
        			
        		}
        	}
        	answer[j] = count;
        	System.out.println(count);
        }
        
        return answer;
    }
	
	public static boolean check(HashMap maps, String[] strList) {
		if(!strList[0].equals("-") && !maps.get("lan").toString().equals(strList[0])) return false;
		if(!strList[1].equals("-") && !maps.get("group").toString().equals(strList[1])) return false;
		if(!strList[2].equals("-") && !maps.get("career").toString().equals(strList[2])) return false;
		if(!strList[3].equals("-") && !maps.get("food").toString().equals(strList[3])) return false;
		if(Integer.parseInt((String)maps.get("score")) < Integer.parseInt(strList[4])) return false;
		return true;
	}
	
}
