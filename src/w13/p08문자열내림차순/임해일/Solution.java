package w13.p08문자열내림차순.임해일;

class Solution {
    public String solution(String s) {
        StringBuffer sb = new StringBuffer();
        char[] arr = s.toCharArray();
        for (char c = 'z'; c >= 'A'; c--) {
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == c) {
                    sb.append(c);
                }
            }
        }
        String answer = sb.toString();

        return answer;
    }
}