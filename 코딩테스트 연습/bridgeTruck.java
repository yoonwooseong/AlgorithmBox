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
		
		//queue�� �ֱ�
		for(int i = 0; i < truck_weights.length; i++) {
			queue.add(truck_weights[i]);
			eachTime[i] = bridge_length;
		}
		
		while(true) {

			//�ٸ� �ǳʴ� Ʈ���� ��� Ʈ���� ������ ����
			if(queue.size() == 0 && bridge.size() == 0) {
				break;
			}
			//�ð�
			count++;
			
			//�� Ʈ���� �ð� -1
			for(int i = start; i < start+bridge.size(); i++) {
				eachTime[i] = eachTime[i]-1;
				if(eachTime[i] == 0) {
					bridge.remove(0);
					start++;
				}
			}
			
			//�ٸ��� �ִ� ���� + ���� �� Ʈ���� ���԰� �ߵ�� �������� �۰ų� ������ �̵�
			if(queue.size() != 0) {
				if(bridge.stream().mapToInt(Integer::intValue).sum()+queue.peek() <= weight) {
					bridge.add(queue.poll());
				}				
			}
		}
		return count;
    }
}