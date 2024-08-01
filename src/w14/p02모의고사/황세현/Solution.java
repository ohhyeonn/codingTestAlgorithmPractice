package w14.p02모의고사.황세현;

import java.util.*;

import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] st1 = {1,2,3,4,5}; // 5
        int[] st2 = {2, 1, 2, 3, 2, 4, 2, 5}; //8
        int[] st3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}; // 10
        int[] a = new int[3];
        for(int i = 0; i<answers.length; i++){
            if(st1[i%5] == answers[i]){ a[0]++;}
            if(st2[i%8] == answers[i]){ a[1]++;}
            if(st3[i%10] == answers[i]){ a[2]++;}
        }
        int maxScore = 0;
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for(int i =0; i<3; i++){
            if(maxScore<a[i]){
                maxScore = a[i];
                answer.clear();
                answer.add(i+1);

            }else if (maxScore == a[i]){
                answer.add(i+1);
            }

        }
        return answer.stream().mapToInt(i -> i).toArray();

    }
}