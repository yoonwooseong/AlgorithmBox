package test;

import java.util.ArrayList;
import java.util.HashSet;

public class PonKemon {
	public static void main(String[] args) {
		int[] a = {3,1,2,3};
		solution(a);
	}
	public static int solution(int[] nums) {
        int answer = 0;
        
        HashSet<Integer> set = new HashSet<Integer>();
        
        for(int i = 0; i < nums.length; i++) {
        	set.add(nums[i]);
        }
        
        return set.size() < nums.length/2 ? set.size():nums.length/2;

    }
}
