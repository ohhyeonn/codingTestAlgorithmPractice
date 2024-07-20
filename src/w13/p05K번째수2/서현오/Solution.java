package w13.p05K번째수2.서현오;


import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        
        for(int a = 0; a < commands.length; a++){
            
            int i = commands[a][0];
            int j = commands[a][1];
            int k = commands[a][2];
            int[] tempArray = new int[j+1-i];
            int c = 0;
            for(int b = i-1; b <j; b++){
                tempArray[c] = array[b];
                c++;
            }
            
            Arrays.sort(tempArray);
            
            answer[a] = tempArray[k-1];
            
            
        }
        
        
        
        
        return answer;
    }
}