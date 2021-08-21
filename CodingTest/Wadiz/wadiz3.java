package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;

public class wadiz3 {
	HashMap<Integer,String> map = new HashMap<>();
	
	public static void main(String[] args) {
		int[] arr = {1, 2, 4, 8, 4, 2, 1};
		System.out.println(solution(arr));
	}
	
	static int[] arrResult;
	static int[] arrValue;
	static boolean[] complete;
	
	
	public static int solution(int[] arr) {
		int count = 0;
		int arrSize = arr.length;
		arrResult = new int[arrSize];
		complete = new boolean[arrSize];
		arrValue = arr;
		
		
		int value2 = min(arr, arrSize);
		System.out.println(value2);
		for(int j = 0; j < arrSize ; j++) {
			arrResult[j] += value2;
			System.out.println(arrResult[j]);
		}
		
		minus(arrValue, value2);
		
		for(int j = 0; j < arrSize ; j++) {
			
			System.out.println(arrResult[j]);
		}
		
		while(true) {
			check(arr, arrResult);
			if(allCheck(complete)) {
				return count;
			}
			for(int i = 0; i < complete.length; i++) {
//				System.out.println(complete[i]);
			}
			
			
			for(int i = 0; i < arr.length; i++) {
				
				if(complete[i] == true) {
					if(i >= 1) {
						int value = min(arrValue, i-1);
						for(int j = 0; j < i ; j++) {
							if(complete[i] == false) {
								arrResult[j] += value;							
							}
						}
						minus(arrValue, value);
					}
				}
			}
			count ++;
		}
    }
	
	private static void check(int[] arr, int[] arrResult) {
		for(int i=0;i<arr.length;i++) {
		    if(arr[i] == arrResult[i]) {
		    	complete[i] = true;
		    }
		}
		return;
	}
	
	private static int min(int[] arr, int index) {
		int min = 1000000000; //최소값
		for(int i=0;i<index;i++) {
		    if(arr[i] > 0 && min>arr[i]) {
		    	min = arr[i];
		    }
		}
		return min;
	}
	
	private static boolean allCheck(boolean[] complete) {
		for(int i=0;i<complete.length;i++) {
			if(!complete[i]) {
				return false;
			}
		}
		return true;
	}
	
	private static void minus(int[] arrValue, int value) {
		for(int i=0;i<arrValue.length;i++) {
			arrValue[i] -= value;
		}
		return;
	}
	
	
}
