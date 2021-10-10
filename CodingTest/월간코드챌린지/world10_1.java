package test;

import java.util.ArrayList;
import java.util.HashSet;

public class world6 {
	public static void main(String[] args) {
		int n = 10;
		solution(n);
	}
	public static int solution(int n) {
        int answer = 0;
        int n2 = n - 1;
        
        for(int i = 1; i < n; i++) {
        	if((n2%i) == 0) {
        		return i;
        	}
        }
        return n;
    }
}
