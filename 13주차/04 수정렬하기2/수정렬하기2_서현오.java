import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(bf.readLine());
		int[] array = new int[n];
		for(int i = 0; i < n; i++) {
			array[i] = Integer.parseInt(bf.readLine());
		}
		
		Arrays.sort(array);
		
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < n; i++) {
			sb.append(array[i]);
			sb.append("\n");
		}
		
		
		System.out.println(sb.toString());
	}

}