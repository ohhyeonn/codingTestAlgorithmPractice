
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		String line = bf.readLine();
		char[] array = line.toCharArray();
		Arrays.sort(array);
		StringBuilder sb = new StringBuilder(new String(array));
		String reverse = sb.reverse().toString();
	
		System.out.println(reverse);
		
	}

}