package solution;

public class FindDecimalsInK {
	public static void main(String[] args) {
		int answer = solution(120307,10);
		
		System.out.println(answer);
	}
	
	public static int solution(int n, int k) {
        String kDecimal = toKDecimals(n, k); 			 // k진수로 변환
        long[] splitedDecimals = splitDecimal(kDecimal); // 0 기준 배열로 나누기
        
        return countDecimal(splitedDecimals);			 // 소수 갯수 세기
    }
	
	public static String toKDecimals(int n, int k) {
		if(k == 10) return Integer.toString(n);
        String decimal = "";
        
        while(true) {
        	if((long) Math.floor(n/k) == 0) { 			// 더이상 나눌 수 없는 경우
        		decimal = n%k + decimal;
        		break;        		
        	}else {
        		decimal = n%k + decimal;
        		n = (int) Math.floor(n/k);        		
        	}
        }

        return decimal;
    }
	
	public static long[] splitDecimal(String decimal) {
		String[] tempNumbers = decimal.replaceAll("0+", "0").split("0");
		long[] numbers = new long[tempNumbers.length];
		
		for(int i = 0; i < tempNumbers.length; i++) {
			numbers[i] = Long.parseLong(tempNumbers[i]);
		}
	
        return numbers;
    }

	public static int countDecimal(long[] numbers) {
		int answer = 0;
        for(int i = 0; i < numbers.length; i++) {
        	if(isDecimal(numbers[i])) {
        		answer++;
        	}
        }
		return answer;
    }
	
	public static boolean isDecimal(long number) {
		if(number == 1) return false;
		
		for(int i=2; i<=Math.sqrt(number); i++) {
			if(number%i == 0) return false;
		}
		return true;
    }
}
