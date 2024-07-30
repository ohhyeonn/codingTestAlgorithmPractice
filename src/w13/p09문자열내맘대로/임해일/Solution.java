package w13.p09문자열내맘대로.임해일;

import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = strings;
        Arrays.sort(answer);
        Arrays.sort(answer, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String sub1 = o1.substring(n, n + 1);
                String sub2 = o2.substring(n, n + 1);
                int result = sub1.compareTo(sub2);
                return result;
            }
        });
        return answer;
    }
}