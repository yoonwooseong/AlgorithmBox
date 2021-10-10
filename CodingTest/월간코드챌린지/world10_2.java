package test;

import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.Stream;

public class world7 {
	public static void main(String[] args) {
		int n = 3;
		int left = 2;
		int right = 5;
		solution(n, left, right);
		System.out.println(square[2][2]);
	}
	static int[][] square;
	
	public static int[] solution(int n, long left, long right) {
		square = new int[n][n];
		
int[] answer = new int[(int) (right - left + 1)];
        
        for(int i = n; i > 0; i--) {
        	for(int j = n-1; j >= 0; j--) {
            	for(int k = n-1; k >= 0; k--) {
            		System.out.println(n);
        			square[j][k] = n;
            	}
            }
        	n = n - 1;
        }
        int index = 0;
		int col = square.length;
		int row = square[0].length;
		int arr[] = new int[col * row];
		
		for(int i = 0; i < square.length; i ++) {	
			for(int j= 0; j< square[0].length; j ++) {
				arr[ i * square[0].length + j] = square[i][j];
			}
		}
		
		int index2 = 0;
		int index3 = 0;
		for (int i : arr) {
			if(index2 > right) {
				return answer;
			}
			
			if(index3 >= left && index3 <= right) {
				answer[index2] = i;
				index2 ++;
			}
			index3++;
		}
        return answer;
    }
	
	
}
