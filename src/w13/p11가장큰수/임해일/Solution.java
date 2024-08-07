package w13.p11가장큰수.임해일;

import java.util.PriorityQueue;

public class Solution {
    public static void main(String[] args) {
        int[] test = new int[]{3, 30, 34, 5, 9};
        int[] test2 = new int[]{6, 10, 2};
        System.out.println(
                solution(test)
        );
    }

    public static String solution(int[] numbers) {
        String answer = "";
        PriorityQueue<String> pq = new PriorityQueue<>((a, b) -> {
            String temp1 = a + b;
            String temp2 = b + a;
            return temp2.compareTo(temp1);
        });
        for (int i : numbers) {
            pq.offer(String.valueOf(i));
        }
        // 우선순위 큐를 이용해 가장 큰 수를 만든다
        StringBuilder sb = new StringBuilder();
        while (!pq.isEmpty()) {
            sb.append(pq.poll());
        }

        // 만약 가장 큰 수가 0으로 시작하면 "0"을 반환
        answer = sb.toString();
        if (answer.charAt(0) == '0') {
            return "0";
        }

        return answer;
    }
}
