package w14.p04소수찾기.서현오;

import java.util.*;

class Solution {
    
    
    public static int totalCount = 0;
    public static ArrayList<Integer> list = new ArrayList<>();
    
    public int solution(String numbers) {
        String[] array = numbers.split("");
        for(int i = 1; i <= array.length ; i++){
            combination(array , new boolean[array.length] , new String[i] , 0 , i); 
        }
        
        
        
        
        return totalCount;
    }
    
    
    public static void combination(String[] array , boolean[] visited , String[] out , int depth , int r){
        if(depth == r){
            
            StringBuilder sb = new StringBuilder();
            
            for(int i = 0; i < out.length ; i++){
                sb.append(out[i]);
            }
            int number = Integer.parseInt(sb.toString());
            
            if(!list.contains(number) && check(number)){
                list.add(number);
                
                totalCount++;
            }
            
            return;
            
        }
        
        for(int i = 0; i < array.length ; i++){
            if(!visited[i]){
                visited[i] = true;
                out[depth] = array[i];
                combination(array , visited , out , depth + 1 , r);
                visited[i] = false;
            }
        }
        
        
        
    }
    
    
    public static boolean check(int number){
                
        
        if(number == 0 || number == 1){
            return false;
        }
        
        
        
        for(int i = 2; i < number; i++){
            if(number % i == 0){
                return false;
            }
        }
        
        return true;
        
        
        
        
    }
    
    
}