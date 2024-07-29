package w13.p11가장큰수.서현오;
import java.util.*;

class Solution {
    public String solution(int[] numbers) {
    	

        String[] strArray = new String[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            strArray[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(strArray,(o1 , o2) ->(o2 + o1).compareTo((o1+o2)));
        StringBuilder sb = new StringBuilder();
        if (strArray[0].equals("0")) {
            return "0";
        }
        for(String a : strArray) {
            sb.append(a);
        }
        
        
        return sb.toString();
    }
}