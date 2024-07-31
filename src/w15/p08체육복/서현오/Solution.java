package w15.p08체육복.서현오;
import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] cloth = new int[n];
        Arrays.fill(cloth , 1);
        
        for(int i =0; i < reserve.length; i++){
            cloth[reserve[i]-1] += 1;
        }
        
        for(int i = 0; i < lost.length; i++){
            cloth[lost[i]-1] -= 1;
        }
        
        for(int i = 0; i < cloth.length; i++){
            
            if(cloth[i] == 2){
                if(i == 0){
                    if(cloth[i+1] == 0) {
                        cloth[i+1] = 1;
                        cloth[i] -= 1;
                    }
                }else if (i == cloth.length-1){
                    if(cloth[i-1] == 0){
                        cloth[i-1] = 1;
                        cloth[i] -= 1;
                    }
                }else {
                    if(cloth[i-1] == 0){
                        cloth[i-1] = 1;
                        cloth[i] -= 1;
                        continue;
                    }
                    if(cloth[i+1] == 0) {
                        cloth[i+1] = 1;
                        cloth[i] -= 1;
                        continue;
                    }
                    
                    
                }
                
            }
            
        }
        
        int sum = 0;
        for(int i = 0; i < cloth.length ; i ++){
            if(cloth[i] > 0){
                sum++;
            }
            
        }
        
        
        
        
        
        
        return sum;
    }
}