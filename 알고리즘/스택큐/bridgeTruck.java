package test;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class bridgeTruck {
	
	public static void main(String[] args) {
		int[] i = {7, 4, 5 ,6};
		int result = solution(2, 10, i);

		System.out.println(result);
	}
	
	public static int solution(int bridge_length, int weight, int[] truck_weights) {
        
		Queue<Integer> queue = new LinkedList<>();
		List<Integer> bridge = new ArrayList<>();
		int[] eachTime = new int[truck_weights.length];
		
		int start = 0;
		int count = 0;
		
		//queue에 넣기
		for(int i = 0; i < truck_weights.length; i++) {
			queue.add(truck_weights[i]);
			eachTime[i] = bridge_length;
		}
		
		while(true) {

			//다리 건너는 트럭과 대기 트럭이 없으면 멈춤
			if(queue.size() == 0 && bridge.size() == 0) {
				break;
			}
			//시간
			count++;
			
			//각 트럭의 시간 -1
			for(int i = start; i < start+bridge.size(); i++) {
				eachTime[i] = eachTime[i]-1;
				if(eachTime[i] == 0) {
					bridge.remove(0);
					start++;
				}
			}
			
			//다리에 있는 무게 + 다음 올 트럭의 무게가 견디는 무개보다 작거나 같으면 이동
			if(queue.size() != 0) {
				if(bridge.stream().mapToInt(Integer::intValue).sum()+queue.peek() <= weight) {
					bridge.add(queue.poll());
				}				
			}
		}
		return count;
    }
}