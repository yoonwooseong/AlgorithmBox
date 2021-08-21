package test;

import java.util.Arrays;
import java.util.Collections;

public class wadiz1 {
	public static void main(String[] args) {
		int[][] passwords = {{101,9999},{102,1111}};
		String s = "101#9999#102#1111#101#9999#101#9999#";
		System.out.println(solution(passwords, s));
	}
	
	public static int solution(int[][] passwords, String s) {
		int answer = 0;
		String[] sList = s.split("#");
		int sListSize = sList.length;
		for(int i = 0; i < sListSize; i++) {
			if(check(passwords, Integer.parseInt(sList[i]), 0)) {
				try {
					if(check(passwords, Integer.parseInt(sList[i+1]), 1)) {//(i+1) < sListSize-1 && 
						System.out.println(""+sList[i]+" : "+sList[i+1]);
						answer++;
						i++;
					}
				} catch (Exception e) {
					// TODO: handle exception
				}
			}
		}
        return answer;
    }
	
	private static boolean check(int[][] passwords, int checkNum, int type) {
		int passwordSize = passwords.length;
		for(int i = 0; i < passwordSize; i++ ) {
			if(passwords[i][type] == checkNum) {
				return true;
			}
		}
		return false;
	}
}
