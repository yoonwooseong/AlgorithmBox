package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class naver2 {
	public static void main(String[] args) {
		String s = "abcxyqwertyxyabc";
		System.out.println(solution(s));
	}
	
	public static String[] solution(String s) {
		String[] result = {};
		String frontStr = "";
		String backStr = "";
		
		ArrayList resultList = new ArrayList();
        StringBuilder str = new StringBuilder(s);
        
        int lastIndex = str.length();
        
        for(int i =0; i < lastIndex; i++) {
        	frontStr += str.charAt(i);
        	backStr = str.charAt(lastIndex-1-i)+backStr;
        	if(frontStr.equals(backStr)) {
        		resultList.add(frontStr);
        		frontStr = "";
        		backStr = "";
        	}
        }
        //resultList.addAll(saveList);
        for(int i = 0; i < resultList.size(); i++) {
        	System.out.println(resultList.get(i).toString());
        }
        return result;
    }
	
	
}
