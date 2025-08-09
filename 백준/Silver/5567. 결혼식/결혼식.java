import java.util.*;
import java.io.*;

public class Main {
	
	static List<Integer>[] arr;
	static boolean[] check;
	static int count;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		check = new boolean[n+1];
		
		arr = new ArrayList[n+1];
		for (int i = 0; i < n+1; i++) {
			arr[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			
			int n1 = Integer.parseInt(st.nextToken());
			int n2 = Integer.parseInt(st.nextToken());
			arr[n1].add(n2);
			arr[n2].add(n1);
		}
		
		dfs(0, 1);//(depth, start)
		
		for (int i = 2; i < check.length; i++) {
			if(check[i]) count += 1;
		}
		
		System.out.println(count);
		
	}
	
	public static void dfs(int depth, int start) { // 01 , 1 2, 2 3 , 
		if(depth == 2) return;
		
		for (int i : arr[start]) {
			
			check[i] = true;
			dfs(depth+1, i);
			
		}
		
		
	}
	
	
}