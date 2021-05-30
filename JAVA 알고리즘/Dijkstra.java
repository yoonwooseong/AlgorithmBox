package test;

public class Dijkstra {
	
	private static final int MY_LOCATION = 1;
	private static final int DESTINATION = 5;
	private static final int START = 0;
	private static final int END = 1;
	private static final int DISTANCE = 2;
	
	public static void main(String[] args) {
	   int N = 5;
	   int[][] road = {{1,2,1},{2,3,3},{5,2,2},{1,4,2},{5,3,1},{5,4,2}};
	   int result = solution(N, road);
	   System.out.println(result);
	}
	
	public static int solution(int n, int[][] road) {
		
		int maps[][] = new int[n+1][n+1];
		int distance[] = new int[n+1];
		boolean[] check = new boolean[n+1];
		
		for(int i=1; i<n+1; i++) {
			distance[i] = Integer.MAX_VALUE;
		}
		
		for(int i=0; i <road.length; i++) {
			maps[road[i][START]][road[i][END]] = road[i][DISTANCE];
			maps[road[i][END]][road[i][START]] = road[i][DISTANCE];
		}

		//시작점 Set
		distance[MY_LOCATION] = 0;
		check[MY_LOCATION] = true;
		
		for(int i=1;i<n+1;i++) {
			if(!check[i] && maps[MY_LOCATION][i] != 0) {//값 0 은 Null 의미
				distance[i] = maps[MY_LOCATION][i];
			}
		}
		
		//탐색 시작
		for(int t=0; t<n-1; t++) {
			int min_distance = Integer.MAX_VALUE;
			int min_index = -1;
			
			for(int i=1;i<n+1;i++) {
				if(!check[i] && distance[i]!=Integer.MAX_VALUE) {
					if(distance[i]<min_distance) {
						min_distance = distance[i];
						min_index = i;
					}
				}
			}
			
			check[min_index] = true;
			
			for(int i=1; i<n+1; i++) {
				if(!check[i] && maps[min_index][i] != 0) {
					if(distance[i] > distance[min_index]+maps[min_index][i]) {
						distance[i] = distance[min_index]+maps[min_index][i];
					}
				}
			}
			 for(int i=1;i<n+1;i++){
		            System.out.print(distance[i]+" ");
		        }
		        System.out.println("");


		
		}

        return distance[DESTINATION];
    }
}
