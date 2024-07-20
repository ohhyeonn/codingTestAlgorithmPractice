import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		String[] line = bf.readLine().split(" ");
		int[] intLine = Arrays.stream(line).mapToInt(Integer :: parseInt).toArray();

		Arrays.sort(intLine);
		int sum = 0;
		for(int i = 0; i <n; i++) {
			for(int j = 0; j <= i ; j++ ) {
				sum += intLine[j];
			}
		}
		System.out.println(sum);
		
		
	}

}