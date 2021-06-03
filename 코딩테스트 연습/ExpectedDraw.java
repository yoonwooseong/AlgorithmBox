package test;

public class ExpectedDraw {
	public static int solution(int n, int a, int b)
    {
        int answer = 1;
        int roomA = (int)Math.ceil((float)a/2);
        int roomB = (int)Math.ceil((float)b/2);
        while(roomA != roomB){
            roomA = (int)Math.ceil((float)roomA/2);
            roomB = (int)Math.ceil((float)roomB/2);

            answer++;
        }
        return answer;
    }
}
