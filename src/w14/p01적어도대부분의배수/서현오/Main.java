package w14.p01적어도대부분의배수.서현오;
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] array = bf.readLine().split(" ");
		int[] intArray = new int[array.length];
		
		for(int i = 0 ; i < array.length ; i++) {
			intArray[i] = Integer.parseInt(array[i]);
		}
		
		int number = 0;
		for(int i = 1 ; i < 100000000 ; i++) {
			int count = 0;
			
			if(i % intArray[0] == 0) {
				count++;
			}
			if(i % intArray[1] == 0) {
				count++;
			}
			if(i % intArray[2] == 0) {
				count++;
			}
			if(i % intArray[3] == 0) {
				count++;
			}
			if(i % intArray[4] == 0) {
				count++;
			}
			
			
			if(count >= 3) {
				number = i;
				break;
			}
			
		}
		
		
		System.out.println(number);
		

	}

}
