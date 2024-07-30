package w13.p05K번째수2.임해일;

import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] array =  {1,5,2,6,3,7,4};
        int[][] commands = {{2,5,3},{4,4,1},{1,7,3}};
        int[] answer = solution(array, commands);
        for(int i : answer) {
            System.out.println(i);
        }
    }

    public static int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i = 0; i < commands.length; i++) {
            if(commands[i][0] == commands[i][1]) {
                answer[i] = array[commands[i][0] - 1];
            }
            else {
                int[] temp = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
                Arrays.sort(temp);
                answer[i] = temp[commands[i][2] - 1];
            }
        }
        return answer;
    }
}
