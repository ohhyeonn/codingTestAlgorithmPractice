package w14.p03카펫.서현오;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        for(int i = 1; i <= yellow ;i++){
            //세로가 1줄일때 2 ... 3 ...
            // 가로
            int x = 0;
            if(yellow % i == 0){
               x =   yellow / i;
            }else {
                continue;
            }
            
            // 세로
            int y = i;
                
                
                
            int sum = 0;
            
            sum = (x * 2) + (y * 2) + 4;
            
            if(sum == brown){
                answer[0] = x+2;
                answer[1] = y+2;
                break;
            }
        }
        
        
        
        
        return answer;
    }
}