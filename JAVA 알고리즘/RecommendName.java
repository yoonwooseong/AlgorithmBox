package solution;

import java.util.Arrays;

public class RecommendName {	
	public static void main(String[] args) {
		String newname = "abcdefghijklmn.p";
		
		solution(newname);
	}
	public static String solution(String new_id) {
        String answer = "";
        new_id = new_id.toLowerCase();
        new_id = removeOtherCase(new_id);
        new_id = new_id.replaceAll("\\.+", ".");
        new_id = removeEdgeDot(new_id);
        new_id = new_id.replaceAll(" ", "a");
        new_id = maxLength15(new_id);
        new_id = leastLength3(new_id);
        
        
        System.out.println("´ä : "+new_id);
        return answer;
    }
	
	public static String removeOtherCase(String new_id) {
		Character[] useChar = {'-','_','.'};
		String removedString = ""; 
		for(int i = 0; i < new_id.length(); i++) {
			char ch = new_id.charAt(i);
			if(Arrays.asList(useChar).contains(ch) || isLower(ch) || isNumber(ch)) {
				removedString += ch;
			}
		}
		return removedString;		
	}
	public static boolean isLower(char ch) {
		return 'a' <= ch && ch <= 'z' ? true:false;		
	}
	public static boolean isNumber(char ch) {
		return '0' <= ch && ch <= '9' ? true:false;		
	}
	
	public static String removeEdgeDot(String str) {		
		if(str.length() > 0 && str.charAt(0) == '.') str = str.substring(1);
		if(str.length() > 0 && str.charAt(str.length()-1) == '.') str = str.substring(0,str.length()-1);
		
		if(str.length() == 0) return "a";
		return str;
	}
	public static String maxLength15(String str) {
		if(str.length() > 15) 
			return removeEdgeDot(str.substring(0,15));
		else
			return str;
	}
	public static String leastLength3(String str) {
		if(str.length() > 3) 
			return str;
		else if(0 < str.length() && str.length() <= 2) {
			char lastStr = str.charAt(str.length()-1);
			str += lastStr;
			str = leastLength3(str);
		}
		return str;
	}
}
