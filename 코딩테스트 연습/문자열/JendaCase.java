package test;

import java.util.ArrayList;
import java.util.HashSet;

public class JendaCase {
	public static void main(String[] args) {
		String a = " adgagd 3eagdag ";
		System.out.println(solution(a));
	}
	public static String solution(String s) {
        String[] sList = s.toLowerCase().split("");
        String answer = sList[0].replaceFirst(sList[0].substring(0,1), sList[0].substring(0,1).toUpperCase());

        for(int i = 1; i < sList.length; i++) {
        	if(sList[i-1].equals(" ")) {
        		String c = sList[i].replaceFirst(sList[i].substring(0,1), sList[i].substring(0,1).toUpperCase());
        		answer += c;
        	} else {
        		answer += sList[i];
        	}
        }
        
        return answer;

    }
}
