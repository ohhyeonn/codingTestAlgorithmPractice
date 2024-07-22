package w13.p07Hindex.서현오;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        for(int i = 1000; i >= 1; i--){
            int target = i;
            int count = 0;
            
            for(int j = 0 ; j < citations.length ; j++){
                if( citations[j] >= target){
                    count++;
                }
            }
            
            if(target <= count){
                answer = target;
                break;
            }
            
            
            
            
        }
        
        
        
        
        return answer;
    }
}