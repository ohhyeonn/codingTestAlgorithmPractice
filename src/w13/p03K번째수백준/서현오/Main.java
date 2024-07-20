package w13.p03K번째수백준.서현오;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] firstLine = bf.readLine().split(" ");
		
		int n = Integer.parseInt(firstLine[0]);
		int k = Integer.parseInt(firstLine[1]); 
		int[] intLine = Arrays.stream(bf.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();

		Arrays.sort(intLine);
		System.out.println(intLine[k-1]);
		
		
	}

}
