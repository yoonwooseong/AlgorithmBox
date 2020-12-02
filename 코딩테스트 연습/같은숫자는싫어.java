import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        ArrayList al = new ArrayList();
        int preNum = 10;
        for (int i = 0; i < arr.length; i++) {
            if (preNum != arr[i]) {
                al.add(arr[i]);
            }
            preNum = arr[i];
        }
        int[] answer = new int[al.size()];

        for (int i = 0; i < answer.length; i++) {
            answer[i] = (int) al.get(i);
        }

        return answer;
    }
}