package test;

import java.util.ArrayList;

public class world2 {
	public static void main(String[] args) {
		String[] grid = {"SL","LR"};
		System.out.println(solution(grid)[0]);
	}
	
	static int R, C;
	static boolean[][][] isVisited;
	static int[] dR = {-1, 0, 1, 0}, dC = {0, -1, 0, 1};
	
	public static int[] solution(String[] grid) {
		ArrayList answer = new ArrayList();
		R = grid.length;
		C = grid[0].length();
		isVisited = new boolean[R][C][4];
		
		for(int i = 0; i < R; i++) {
			for(int j = 0; j < C; j++) {
				for(int k = 0; k < 4; k++) {
					if (!isVisited[i][j][k])
                        answer.add(light(grid, i, j, k));
				}
			}
		}
		
		return answer.stream().mapToInt(i->(int)i).toArray();
	}
	private static int light(String[] grid, int r, int c, int d) {
        int cnt = 0; // 이동거리
 
        while (true) {
            if (isVisited[r][c][d])
                break;
 
            cnt++;	// 거리증가
            isVisited[r][c][d] = true; // 방문처리
 
            if (grid[r].charAt(c) == 'L')
                d = (d + 1) % 4; // 좌회전
            else if (grid[r].charAt(c) == 'R')
                d = (d + 3) % 4; // 우회전
 
            r = (r + dR[d] + R) % R;
            c = (c + dC[d] + C) % C;
        }
 
        return cnt;
    }
	
}
