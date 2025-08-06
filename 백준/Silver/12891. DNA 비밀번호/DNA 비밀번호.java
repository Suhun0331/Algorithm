
import java.util.*;
import java.io.*;

public class Main {
	static int n;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int s = Integer.parseInt(st.nextToken());
		int p = Integer.parseInt(st.nextToken());
		
		String str = br.readLine();
		int[] arr = new int[str.length()];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = str.charAt(i);
		}
		st = new StringTokenizer(br.readLine());
		int[] need = new int[4];
		for (int i = 0; i < need.length; i++) {
			need[i] = Integer.parseInt(st.nextToken());
		}
		int a = 0;
		int c = 0;
		int g = 0;
		int t = 0;
		int answer = 0;
		for (int i = 0; i < p; i++) {
			if(arr[i] == 'A') a += 1;
			else if(arr[i] == 'C') c += 1;
			else if(arr[i] == 'G') g += 1;
			else if(arr[i] == 'T') t += 1;
		}
		
		if(need[0] <= a && need[1] <= c &&need[2] <= g &&need[3] <= t) {
			answer += 1;
		}
		
		for (int i = 1; i < s-p+1; i++) {
			if (arr[i-1] == 'A') a -= 1;
			else if (arr[i-1] == 'C') c -= 1;
			else if (arr[i-1] == 'G') g -= 1;
			else if (arr[i-1] == 'T') t -= 1;
			
			if (arr[i+p-1] == 'A') a += 1;
			else if (arr[i+p-1] == 'C') c += 1;
			else if (arr[i+p-1] == 'G') g += 1;
			else if (arr[i+p-1] == 'T') t += 1;
			
			if(need[0] <= a && need[1] <= c &&need[2] <= g &&need[3] <= t) {
				answer += 1;
			}
		}
		
		System.out.print(answer);
		
		
		
		
		
	}
}
