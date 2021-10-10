class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int size = numbers.length;
        for(int i = 0; i < size; i++){
            answer += numbers[i];
        }
        return 45-answer;
    }
}