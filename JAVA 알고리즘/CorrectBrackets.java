package solution;

public class CorrectBrackets {
	public static String u = "";
	public static String v = "";
	
	public static void main(String[] args) {
		String answer = solution("()))((()");
		
		System.out.println(answer);
	}
	
	public static String solution(String w) {
		if(w.equals("")) 			  // 1
			return "";   
		
		division(w); 	   			  // 2
		
		if(isCorrectBracket(u)) { // 3
			return u+solution(v);
		}else{ 				      	  // 4
			return changeCorrectBracket();
		}
    }
	
	public static void division(String input) {
		int inputHalfLength = input.length()/2;
		
		for(int i = 0; i < inputHalfLength; i++) {
			String tempStr = input.substring(0, (i+1)*2);
			int totalLength = tempStr.length();
			int leftLength = tempStr.replaceAll("\\)", "").length();
			int rightLength = totalLength - leftLength;
			
			if(leftLength == rightLength) {
				u = tempStr;
				v = input.substring((i+1)*2);
				return;
			}
		}
		return;
    }
	
	public static String changeCorrectBracket() {
		String tempU = u;
		String result = "("+solution(v)+")";   // 4-1,2,3
		result += reverseBracket(tempU); // 4-4
		
		return result; 						 // 4-5
    }
	
	public static String reverseBracket(String bracket) {
		if(bracket.length() > 2){
			bracket = bracket.substring(1, bracket.length()-1);
		}else{
			return "";
		}
		
		String reversedBracket = "";
		int length = bracket.length();
		for(int i = 0; i < length; i++) {
			if(bracket.charAt(i) == '(') reversedBracket += ")";
			else if(bracket.charAt(i) == ')') reversedBracket += "(";
		}
		
		return reversedBracket;
    }
	
	public static boolean isCorrectBracket(String u) {
		int count = 0; 						// '(' 와 ')'의 갯수 차이; ')'이 더 많이 오는 순간 음수 값
		int tempULength = u.length();
		
		if(tempULength == 0) {
			return true;
		}else {
			for(int i = 0; i < tempULength; i++) {
				if(u.charAt(i) == '(') count++;
				else count--;
				
				if(count < 0) return false;
			}			
		}
		return true;
    }
}
