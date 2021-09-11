package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class kakao2 {
	public static void main(String[] args) {
		int n = 11;
		int k = 10;
		System.out.println(solution(n, k));
	}
	public static int solution(int n, int k) {
		int answer = 0;
		StringBuilder sb = new StringBuilder();
	    int curNum = n;
	    boolean isP = false;
        while(true){
        	if(curNum <= 0) {
        		break;
        	}
            if(curNum % k < 10){
                sb.append(curNum % k);
            } else {
                sb.append((char)(curNum % k - 10 + 'A'));
            }
            curNum /= k;
        }
        String[] newSt = sb.reverse().toString().split("0");

        for(int i = 0; i < newSt.length; i++) {
        	if(!newSt[i].equals("")) {
        		int checkNum = Integer.parseInt(newSt[i]);
        		
        		if(checkNum != 1 && sosu(checkNum)) {
        			answer++;
        		}        		
        	}
        }
        return answer;
        
    }
	
	public static boolean sosu(int num) {
		int num2 = num/2;
		for (int i = 2; i < num2+1; i++) {
            if (num % i == 0) {
                return false;
            }
        }
		return true;
	}
}
