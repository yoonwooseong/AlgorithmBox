package test;

public class KaKaoTest1 {
	
	static String [] arr = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	
	public static void main(String[] args) {
		System.out.println(solution("one4seveneight"));
		//return solution("one4seveneight");
	}
	
	public static int solution(String s) {
        for(int i = 0; i <arr.length; i++) {
        	s = s.replaceAll(String.valueOf(arr[i]),String.valueOf(i));
        }
        return Integer.parseInt(s);
    }
}
