package w14.p07잃어버린괄호.서현오;

import java.util.*;
import java.io.*;


public class Main  {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String aa = bf.readLine();
		String[] minusArray;
		if(aa.contains("-")) {
			minusArray = aa.split("-");
		}else {
			minusArray = new String[]{aa};
		}
		
		int[] intArray = new int[minusArray.length];
		
		
		for(int i = 0; i < minusArray.length; i ++) {
			//String[] plusArray = minusArray[i].split("+");
			String bb = minusArray[i];
			String[] plusArray;
			if(bb.contains("+")) {
				plusArray = bb.split("\\+");
			}else {
				plusArray = new String[]{bb};
			}
			
			
			
			
			
			int sum = 0;
			for(int j = 0; j < plusArray.length; j++) {
				sum += Integer.parseInt( plusArray[j]);
			}
			
			intArray[i] = sum;
		}
		
		int result = intArray[0];
		if(intArray.length > 1) {
			for(int i = 1; i < intArray.length; i++) {
				result -= intArray[i];
			}
		}
		
		System.out.println(result);
		

	}

}
