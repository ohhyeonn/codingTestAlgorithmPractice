package w14.p06코인0.서현오;
//https://www.acmicpc.net/problem/11047

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] line = bf.readLine().split(" ");
		int n = Integer.parseInt(line[0]);
		int k = Integer.parseInt(line[1]);
		
		
		int[] array = new int[n];
		for(int i = 0; i < n; i++) {
			array[i] = Integer.parseInt(bf.readLine());
		}
		int count = 0;
		for(int i = n-1 ; i >= 0; i--) {
			while(true) {
				if(array[i] <= k) {
					count++;
					k -= array[i];
				} else {
					break;
				}
			}
			
		}
		
		
		System.out.println(count);
		
		
		
		
		
	}

}
