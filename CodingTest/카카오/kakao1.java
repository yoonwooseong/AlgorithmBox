package test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class kakao1 {
	public static void main(String[] args) {
		String[] id_list = {"con", "ryan"};
		String[] report = {};
		int k = 2;
		solution(id_list, report, k);
	}
	public static int[] solution(String[] id_list, String[] report, int k) {
		int[] answer = new int[id_list.length];
		int[] rec = new int[id_list.length];
		ArrayList banlist = new ArrayList();
		HashMap map = new HashMap();
		
		for(int i = 0 ; i < id_list.length; i++) {
			ArrayList list = new ArrayList();
			map.put(id_list[i], list);
//			System.out.println(map.get("muzi"));
		}
		
		ArrayList<String> arrayList = new ArrayList<>();

        for(String item : report){
            if(!arrayList.contains(item))
                arrayList.add(item);
        }
        
        String[] array = arrayList.toArray(new String[arrayList.size()]);

		for(int i = 0; i < array.length; i++) {
			System.out.println(array[i]);
		}
        
		for(int i = 0; i < array.length; i++) {
			String[] rep = array[i].split(" ");
				rec[searchIndex(id_list, rep[1])]++;				
			
			ArrayList list2 = new ArrayList(); 
			list2 = (ArrayList)map.get(rep[0]);
//			System.out.println(map.get(rep[0]));
			
			list2.add(rep[1]);
			map.put(rep[0], list2);
		}
		
		
		for(int i = 0; i < rec.length; i++) {
			if(rec[i] >= k) {
				banlist.add(id_list[i]);
			}
		}
		
		for(int i = 0; i < id_list.length; i++) {
			ArrayList inList = (ArrayList) map.get(id_list[i]);
			for(int j = 0; j < banlist.size(); j++){
				if(inList.contains(banlist.get(j))) {
					answer[i]++;
				}
			}
		}
		
		for(int i = 0; i < answer.length; i++) {
			System.out.println(answer[i]);
		}
        return answer;
        
    }
	public static int searchIndex(String[] id_list, String str) {
		int i;
		for(i = 0; i < id_list.length; i++) {
			if(id_list[i].equals(str)) {
				return i;
			}
		}
		return -1;
	}
}
