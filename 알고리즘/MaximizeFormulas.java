package test;

public class MaximizeFormulas {
	public static void main(String[] args) {
        int n = 3;
        String[] arr = {"+", "*", "-"};
        String[] output = new String[n];
        boolean[] visited = new boolean[n];

        perm(arr, output, visited, 0, n, 3);
        System.out.println();
    }

    // 사전순으로 순열 구하기
    // 사용 예시: perm(arr, output, visited, 0, n, 3);
    static void perm(String[] arr, String[] output, boolean[] visited, int depth, int n, int r) {
        if (depth == r) {
            print(output, r);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i] != true) {
                visited[i] = true;
                output[depth] = arr[i];
                perm(arr, output, visited, depth + 1, n, r);
                visited[i] = false;
            }
        }
    }

    // 배열 출력
    static void print(String[] arr, int r) {
        for (int i = 0; i < r; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
    
    static void sol(String[] arr, String str) {
    	String str2 = str;
        
    	for(int i = 0; i<arr.length; i++) {
    		cal(arr[i], str.charAt(str.indexOf(arr[i])-1), str.charAt(str.indexOf(arr[i])+1));
        	str2 = str2.replaceAll(str.substring(str.indexOf(arr[i])-1,str.indexOf(arr[i])+2), Integer.toString(cal(arr[i], str.indexOf(arr[i])-1, str.indexOf(arr[i])+1)));
        }
    }
    
    static int cal(String cal, int n1, int n2) {
    	//연산하기
        switch (cal) {
		case "+":
			return n1 + n2;
		case "-":
			return n1 - n2;
		case "*":
			return n1 * n2;
		default:
			return 0;
		}
    }
    
}
