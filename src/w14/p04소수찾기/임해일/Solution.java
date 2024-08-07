package w14.p04소수찾기.임해일;

import java.util.HashSet;
import java.util.Set;

class Solution {
    Set<Integer> set = new HashSet<>();

    public void recursive(String comb, String others) {
        if (!comb.equals(""))
            set.add(Integer.valueOf(comb));
        for (int i = 0; i < others.length(); i++) {
            recursive(comb + others.charAt(i), others.substring(0, i) + others.substring(i + 1));

        }
    }

    public boolean isPrime(int number) {
        if (number == 0 || number == 1) return false;
        int sqrt = (int) Math.sqrt(number);

        for (int i = 2; i <= sqrt; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }

    public int solution(String numbers) {
        int answer = 0;
        recursive("", numbers);
        for (Integer number : set) {
            if (isPrime(number)) answer++;
        }
        return answer;
    }
}