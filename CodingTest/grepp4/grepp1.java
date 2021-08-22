package test;

import java.util.ArrayList;
import java.util.HashSet;

public class grepp1 {
	public static void main(String[] args) {
		String[] infos = {"kim password", "lee abc"};
		 String[] actions = {"ADD 30", 
				    "LOGIN kim abc", 
				    "LOGIN lee password", 
				    "LOGIN kim password", 
				    "LOGIN kim password", 
				    "LOGIN lee abc", 
				    "ADD 30", 
				    "ORDER",
				    "ORDER",
				    "ADD 40",
				    "ADD 50"};
		solution(infos, actions);
	}
	public static boolean[] solution(String[] infos, String[] actions) {
		int actionsSize = actions.length;

		boolean[] answer = new boolean[actionsSize];
        boolean isLogin = false;
        boolean isAdd = false;
        
        for(int i = 0; i < actionsSize; i++) {
        	if(isLogin == true) {
        		if(actions[i].contains("ADD")) {
        			answer[i] = true;
        			isAdd = true;
        		} else if(isAdd == true && actions[i].contains("ORDER")) {
        			answer[i] = true;
        			isAdd = false;
        		}
        	} else {
        		if(actions[i].contains("LOGIN")) {
        			String[] contents = actions[i].split(" ");
        			String input = contents[1]+" "+contents[2];
        			
        			for(int j = 0; j < infos.length; j++) {
        				if(infos[j].equals(input)) {
        					answer[i] = true;
        					isLogin = true;
        				}
        			}
        		} 
        	}
        }
        
        for(int i = 0 ; i < actionsSize; i++) {
        	System.out.println(answer[i]);
        }
        
        return answer;
    }
}
