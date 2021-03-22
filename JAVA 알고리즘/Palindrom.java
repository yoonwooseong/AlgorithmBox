package test;

import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String in = scanner.next();
		System.out.println(checkPalindrom(in));
		
		scanner.close();
	}
	
	/**
	 * 팰린드롬 체크 
	 * 
	 * @param str
	 * @return
	 */
	private static int checkPalindrom(String str) {
		int j = str.length() - 1;
		for (int i = 0 ; i < str.length()/2; i++, i--) {
			if (str.charAt(i) != str.charAt(j)) {
				return 0;
			}
		}
		return 1;
	}
}
