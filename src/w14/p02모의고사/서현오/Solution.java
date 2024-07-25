package w14.p02모의고사.서현오;

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] first = new int[]{1,2,3,4,5};
        int[] second = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] third = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int firstCount = 0;
        int secondCount = 0;
        int thirdCount = 0;
        for(int i = 0 ; i < answers.length; i++){
            
            if(answers[i] == first[i%5]){
                firstCount++;
            }
            
            if(answers[i] == second[i%8]){
                secondCount++;
            }
            
            if(answers[i] == third[i%10]){
                thirdCount++;
            }
            
        }
        int[] result = new int[3];
        result[0] = firstCount;
        result[1] = secondCount;
        result[2] = thirdCount;
        Arrays.sort(result);
        
        ArrayList<Integer> list = new ArrayList<>();
        
        if(firstCount == result[2]){
            list.add(1);
        }
        if(secondCount == result[2]){
            list.add(2);
        }
        if(thirdCount == result[2]){
            list.add(3);
        }
        
        int[] dap = new int[list.size()];
        
        for(int i = 0; i < list.size() ; i++){
            dap[i] = list.get(i);
        }
        
        
        
        
        
        return dap;
    }
}
