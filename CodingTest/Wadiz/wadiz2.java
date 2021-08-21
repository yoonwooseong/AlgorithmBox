package test;

import java.util.ArrayList;

public class wadiz2 {
	
	public static void main(String[] args) {
		String[] code = {"a=3", "..a=4", "..b=3", "..print a", ".......a=6", ".......print a", ".......print b", "..print a", "....a=7", "....print a", "print a", "print b", "a=4", "print a", "...print a"};
		System.out.println(solution(code));
	}
	
	public static String[] solution(String[] code) {
		ArrayList arrayList = new ArrayList();
		int codeSize = code.length;

		for(int i = 0; i < codeSize; i++) {
			int index = code[i].indexOf("print");
			int printBlockIdx = block(code[i]);
			String s = "";
			
			if(index > -1) {
				
				boolean check = false;
				s = code[i].substring(index+6);
				
				for(int j = i-1; j >= 0 ; j--) {
					int valueBlockIdx = block(code[j]);
					if(printBlockIdx >= valueBlockIdx && code[j].indexOf(s) > -1 && code[j].indexOf("print") == -1) {
//						System.out.println(s+" "+code[j].substring(code[j].indexOf(s)));
						arrayList.add(code[j].substring(code[j].indexOf(s)));
						check = true;
						break;
					}
				}
				if(check == false) {
					arrayList.add("error");
				}
				
			}
		}
		
		
		String[] answer = new String[arrayList.size()];
		int size=0;
		for(int i = 0; i < arrayList.size(); i++){
			answer[size++] = (String)arrayList.get(i);
		}
//		for(int i = 0; i < array.length; i++) {
//			System.out.println(array[i]);
//		}

        return answer;
    }
	
	private static int block(String s) {
		int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '.') count++;
        }
		return count;
	}
	
}
