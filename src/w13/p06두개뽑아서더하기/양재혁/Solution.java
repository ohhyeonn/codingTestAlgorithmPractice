package w13.p06두개뽑아서더하기.양재혁;

import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < numbers.length; i++) {
            map.put(numbers[i], map.getOrDefault(numbers[i], 0) + 1);
        }
        Map<Integer, Integer> result = new HashMap<>();
        for(int num1 : map.keySet()) {
            for(int num2 : map.keySet()) {
                if (!result.containsKey(num1 + num2)) {
                    if (num1 != num2) {
                        result.put(num1 + num2, 1);
                    } else {
                        if (map.get(num1) > 1) {
                            result.put(num1 + num2, 1);
                        }
                    }
                }
            }
        }
        int[] answer = new int[result.keySet().size()];
        int i = 0;
        for(int num : result.keySet()) {
            answer[i++] = num;
        }
        //hash들은 정렬이 되는게 아니라 무작위로 뽑기 때문에 정렬 해줘야함
        Arrays.sort(answer);
        return answer;
    }
}