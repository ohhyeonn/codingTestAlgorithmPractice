package w14.p05메뉴리뉴얼.서현오;

import java.util.*;

class Solution {
    public static ArrayList<String> resultList = new ArrayList<>();
    
    
    public String[] solution(String[] orders, int[] course) {
          for(int i = 0; i < course.length ; i++){
              HashMap<String,Integer> map = new HashMap<>();
              int r = course[i];
              
              for(int j = 0; j < orders.length; j++){
                  String[] order = orders[j].split("");
                  Arrays.sort(order);
                  
                  
                  
                  if(order.length >= r) combination(order , new boolean[order.length] , new String[r] , 0 , 0 , r , map );
                  
              }
              
              ArrayList<String> list = new ArrayList<>(map.keySet());
              if(!list.isEmpty()){
                  Collections.sort(list , (o1 , o2) -> {
                      if(map.get(o2) - map.get(o1) == 0){
                          return o1.compareTo(o2);
                      } else {
                          return map.get(o2) - map.get(o1);
                      }
                                                        } );
                  int maxCount = 0;
                  if(map.get(list.get(0)) >= 2){
                      maxCount = map.get(list.get(0));
                  }
                  for(int k = 0 ; k < list.size() ; k++){
                      System.out.println("key : " + list.get(k) +" value : " + map.get(list.get(k)));
                      
                      
                      if(map.get(list.get(k)) == maxCount){
                          resultList.add(list.get(k));
                      }
                      
                  }
                  
                  
              }
              
              
              
              
              
              
              
              
          }
        
        String[] answer = resultList.stream().toArray(String[] :: new );
        Arrays.sort(answer);
        return  answer;
        
    }
    
    public static void combination(String[] array , boolean[] visited , String[] out , int start , int depth , int r ,HashMap<String,Integer> map){
        if(depth == r){
            String choice = "";
            for(int i = 0; i < out.length ; i++){
                choice = choice + out[i];
            }
            map.put(choice , map.getOrDefault(choice , 0) + 1);
            
           return;
        }
        for(int i = start ; i < array.length ; i ++){
            if(!visited[i]){
                visited[i] = true;
                out[depth] = array[i];
                combination(array , visited , out , i + 1 , depth + 1 , r , map);
                visited[i] = false;
            }
        }
        
    }
    
    
}