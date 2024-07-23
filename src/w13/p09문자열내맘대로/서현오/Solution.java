package w13.p09문자열내맘대로.서현오;
import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        
        Arrays.sort(strings);
        
        Arrays.sort(strings , (a,b) ->a.charAt(n) - b.charAt(n) );
        
        
        
        return strings;
    }
}