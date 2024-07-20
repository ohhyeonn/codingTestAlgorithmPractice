package w13.p06두개뽑아서더하기.서현오;


import java.util.*;

class Solution {
    
    public static ArrayList<Integer> list = new ArrayList<>();
    
    
    public int[] solution(int[] numbers) {
        
        
        combination(numbers , new boolean[numbers.length] , new int[2] , 0 , 0 , 2 );
        int[] answer = list.stream().distinct().sorted().mapToInt(i -> i).toArray();
        
        
        
        return answer;
    }
    
    
    public static void combination (int[] array , boolean[] visited , int[] out , int start , int depth , int r){
        if(depth == r){
            int sum = 0;
            for(int i = 0; i < out.length; i++){
                sum += out[i];
            }
            if(!list.contains(sum)) {
            	list.add(sum);
            }
            return;
        }
        
        for(int i = start; i < array.length; i++) {
        	if(!visited[i]) {
        		visited[i] = true;
        		out[depth] = array[i];
        		combination(array , visited , out , i+1 , depth + 1 , r);
        		visited[i] = false;
        	}
        }
        
    }
}