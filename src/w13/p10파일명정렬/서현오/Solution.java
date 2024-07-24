package w13.p10파일명정렬.서현오;
import java.util.Arrays;
import java.util.regex.*;

//https://school.programmers.co.kr/learn/courses/30/lessons/17686
public class Solution {	
	
    public String[] solution(String[] files) {
    	
    	Arrays.sort(files , (a , b) -> {
    		Pattern pattern = Pattern.compile("^[^1234567890]+");
    		Matcher matcherA = pattern.matcher(a.toUpperCase());
    		Matcher matcherB = pattern.matcher(b.toUpperCase());
    		if(matcherA.find()&&matcherB.find()) {
    			String matcherAgroup = matcherA.group();
    			String matcherBgroup = matcherB.group();
    				
    				if(matcherAgroup.compareTo(matcherBgroup) == 0) {
    					Pattern digitPattern = Pattern.compile("[0123456789]+");
    		    		Matcher digitMatcherA = digitPattern.matcher(a);
    		    		Matcher digitMatcherB = digitPattern.matcher(b);
    		    		
    		    		digitMatcherA.find();
    		    		digitMatcherB.find();
    		    		String A = digitMatcherA.group();
    		    		String B = digitMatcherB.group();
    		    		return Integer.parseInt(A) - Integer.parseInt(B);
    		    		
    		    		
    				}
    			
    			
    			
    				return matcherAgroup.compareTo(matcherBgroup);
    			
    		}
    		return 0;
    	});
    	
    	

    	
    	
        return files;
    }
}