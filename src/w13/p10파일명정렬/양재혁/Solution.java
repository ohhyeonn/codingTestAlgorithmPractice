package w13.p10파일명정렬.양재혁;

public class Solution {
    public String[] solution(String[] files) {
        String[] answer = {};
        String[][] details = new String[files.length][3];
        //나누기
        for(int i = 0; i < files.length; i++) {
            //헤드찾기
            int head = 0;
            int tail = 0;
            boolean found = false;
            for(int j = 0; j < files[i].length(); j++) {
                char c = files[i].charAt(j);
                if(c >= '0' && c <= '9' && !found) {
                    head = j;
                    found = true;
                } else {
                    if(found) {
                        tail = j;
                        break;
                    }
                }
            }
            details[i][0] = files[i].substring(0, head - 1);
            details[i][1] = files[i].substring(head, tail - 1);
            details[i][2] = files[i].substring(tail);
        }
        return answer;
    }
}
