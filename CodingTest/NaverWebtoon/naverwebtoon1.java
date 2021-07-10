package test;

import java.util.Arrays;
import java.util.Collections;

public class naver1 {
	public static void main(String[] args) {
		Integer[] price = {32000,18000,42500};
		Integer[] discounts = {50, 20, 65};
		System.out.println(solution(price, discounts));
	}
	
	public static int solution(Integer[] price, Integer[] discounts) {
        int answer = 0;
        int lastIdx = discounts.length;
        int pricelastIdx = price.length;

        Arrays.sort(discounts,Collections.reverseOrder());
        Arrays.sort(price,Collections.reverseOrder());
        
        for(int i = 0; i < lastIdx; i++) answer += price[i] - price[i]*discounts[i]/100;
        for(int i = lastIdx; i < pricelastIdx; i++) answer += price[i];
        
        return answer;
    }
	
	
}
