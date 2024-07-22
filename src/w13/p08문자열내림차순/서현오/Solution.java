package w13.p08문자열내림차순.서현오;

import java.util.*;


class Solution {
    public String solution(String s) {
        char[] array = s.toCharArray();
        Arrays.sort(array);
        String a = new String(array);
        StringBuilder sb = new StringBuilder(a);
        
        return sb.reverse().toString();
        

    }
}