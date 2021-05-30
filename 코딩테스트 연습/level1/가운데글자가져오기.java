class Solution {
    public String solution(String s) {
        String answer = "";
        int num = s.length();
        if (num % 2 == 0) {
            answer = "" + s.charAt((int) num / 2 - 1) + s.charAt((int) num / 2);
        } else {
            answer = "" + s.charAt((int) num / 2);
        }
        return answer;
    }
}
'''
return word.substring((word.length()-1) / 2, word.length()/2 + 1);  
'''