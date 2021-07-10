package test;

public class naver3 {
	public static void main(String[] args) {
		String s = "aaaaabbbbb";
		String t = "ab";
		System.out.println(solution(s, t));
	}
	
	public static int solution(String s, String t) {
        int answer = 0;
        while(s.contains(t)) {
        	s = s.replaceFirst(t, "");
        	answer++;
        }
        return answer;
    }
	
	
}
