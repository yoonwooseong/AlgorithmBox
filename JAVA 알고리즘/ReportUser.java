package solution;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ReportUser {
	public static Map<String, ArrayList> userInfo = new HashMap<String, ArrayList>();
	public static Map<String, Integer> receiveEmail = new HashMap<String, Integer>();
	public static int CHANCE = 0;
	
	public static void main(String[] args) {
		String[] id_list = {"con", "ryan"};
		String[] report = {"ryan con", "ryan con", "ryan con", "ryan con"};
		int k = 3;
		
		solution(id_list, report, k);
	}
	
	public static int[] solution(String[] id_list, String[] report, int k) {
		setUserNRule(id_list, k);
		processReport(report);
		findOverKUser();
		
        return getEmailCountList(id_list);
    }
	
	public static void setUserNRule(String[] id_list, int k) {
		CHANCE = k;
		int totalUserLength = id_list.length;
		for(int i = 0; i < totalUserLength; i++ ) {
			ArrayList fromUser = new ArrayList();
			userInfo.put(id_list[i], fromUser);			
			receiveEmail.put(id_list[i], 0);
		}
    }
	
	public static void processReport(String[] report) {
		int totalReportLength = report.length;
		for(int i = 0; i < totalReportLength; i++ ) {
			String[] content = report[i].split(" ");
			String fromUser = content[0];
			String toUser = content[1];
			
			ArrayList reportedUserList = (ArrayList) userInfo.get(toUser);			
			if(!reportedUserList.contains(fromUser)) {
				reportedUserList.add(fromUser);				
			}
			userInfo.put(toUser, reportedUserList);
		}
    }
	
	public static void findOverKUser() {
		for(String username : userInfo.keySet()) {
			if(isOverK(username)) countEmail(username);
		}
    }
	
	public static boolean isOverK(String username) {
		ArrayList fromUsers = userInfo.get(username);
		
		return CHANCE <= fromUsers.size()?true:false;
    }
	
	public static void countEmail(String username) {
		ArrayList savedUserList = (ArrayList) userInfo.get(username);
		int totalUserCount = savedUserList.size();
		for(int i = 0; i < totalUserCount; i++) {
			int chance = receiveEmail.get(savedUserList.get(i));
			receiveEmail.put((String) savedUserList.get(i), ++chance);	
		}
    }
	
	public static int[] getEmailCountList(String[] list) {
		int[] result = new int[list.length];
		for(int i = 0; i < list.length; i++) {
			result[i] = receiveEmail.get(list[i]);
			System.out.println(result[i]);
		}
		
		return result;
    }
}
