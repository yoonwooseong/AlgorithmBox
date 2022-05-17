package solution;

public class RankLotto {
	public static int zeroLength = 0;
	
	public static void main(String[] args) {
		int[] lottos = {44, 1, 0, 0, 31, 25};
		int[] win_nums = {31, 10, 45, 1, 6, 19}; // 3 5
		
		solution(lottos, win_nums);
	}
	
	public static int[] solution(int[] lottos, int[] win_nums) {
		int correctNumber = checkLotto(removeZero(lottos), win_nums);
        
        return checkRank(correctNumber);
    }
	
	public static int checkLotto(int[] newLotto, int[] win_nums) {
        int newLottoLength = newLotto.length;
        int correctNumber = 0;
        
		for(int i = 0; i < newLottoLength; i++) {
			int key = newLotto[i];
			
			for(int j = 0; j < win_nums.length; j++) {
				if(win_nums[j] == key) {
					correctNumber++;
					break;
				}				
			}
        }
		
        return correctNumber;
    }
	
	public static int[] removeZero(int[] lottos) {
        int lottosLength = lottos.length;
        int zeroLength = countZero(lottos);
        int[] lottoWithoutZero = new int[lottosLength - zeroLength];
        int newLottoIndex = 0;
        
        for(int i = 0; i < lottosLength; i++) {
        	if(lottos[i] != 0) {
        		lottoWithoutZero[newLottoIndex++] = lottos[i];
        	}
        }
        
        return lottoWithoutZero;
    }
	
	public static int countZero(int[] lottos) {
        int lottosLength = lottos.length;
        int count = 0;
        
        for(int i = 0; i < lottosLength; i++) {
        	if(lottos[i] == 0) {
        		count++;        		
        	}
        }
        
        zeroLength = count;
        return count;
    }
	
	public static int[] checkRank(int correctNumber) {
		int maxNumber = correctNumber + zeroLength;
		int minNumber = correctNumber;
		int maxLank = 1;
		int minLank = 6;
		
		maxLank = maxNumber < 2 ? 6 : 7 - maxNumber;
		minLank = minNumber < 2 ? 6 : 7 - minNumber;
		
		int[] rank = {maxLank, minLank};
        return rank;
    }
	
}
