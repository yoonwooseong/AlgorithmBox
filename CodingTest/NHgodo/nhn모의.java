import java.awt.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
	private static void solution(int sizeOfMatrix, int[][] matrix) {
		// TODO: 이곳에 코드를 작성하세요.
		ArrayList ans = new ArrayList();
		int[] dx = {0, 1 , 0, -1};
		int[] dy = {1, 0 , -1, 0};
		boolean[][] visited = new boolean[11][11];
		Queue<int[]> q = new LinkedList<int[]>();
		
		for(int i = 0; i < matrix.length; i++){
			for(int j = 0; j < matrix[i].length; j++){
				
				if(matrix[i][j] == 1 && visited[i][j] == false) {
					int count = 0;
					int[] xy = {i, j};
					q.add(xy);
					visited[i][j] = true;
					while(q.peek() != null) {
						int[] pollxy = q.poll();
						int nx = pollxy[0];
						int ny = pollxy[1];
						count++;
						for(int k = 0; k < 4; k++) {
							int nextX = nx + dx[k];
							int nextY = ny + dy[k];
							if(nextX < sizeOfMatrix && nextX >= 0 && nextY >= 0 && nextY < sizeOfMatrix) {
								if(matrix[nextX][nextY] == 1 && visited[nextX][nextY] == false) {
									int[] nextxy = {nextX, nextY};
									q.add(nextxy);
									visited[nextX][nextY] = true;
								}
							}
						}
					}
					ans.add(count);	
				}				
			}
		}
		System.out.println(ans.size());
		if(ans.size()!=0) {
			Collections.sort(ans);
			for(int i = 0; i < ans.size(); i++) {
				System.out.printf("%d ",ans.get(i));
			}
		}
	}

	private static class InputData {
		int sizeOfMatrix;
		int[][] matrix;
	}

	private static InputData processStdin() {
		InputData inputData = new InputData();

		try (Scanner scanner = new Scanner(System.in)) {
			inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));      

			inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
			for (int i = 0; i < inputData.sizeOfMatrix; i++) {
				String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
				for (int j = 0; j < inputData.sizeOfMatrix; j++) {
					inputData.matrix[i][j] = Integer.parseInt(buf[j]);
				}
			}
		} catch (Exception e) {
			throw e;
		}

		return inputData;
	}

	public static void main(String[] args) throws Exception {
		InputData inputData = processStdin();

		solution(inputData.sizeOfMatrix, inputData.matrix);
	}
}