import java.util.*;
import java.io.*;

public class Main {
	
	static List<Integer>[] arr;
	static int[] count;
	static int subcount;
	static boolean[] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		count = new int[n+1];
		arr = new ArrayList[n+1];
		subcount = 0;
		int max = 0;
		
		for (int i = 0; i < arr.length; i++) {
			arr[i] = new ArrayList<>();
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int n1 = Integer.parseInt(st.nextToken());
			int n2 = Integer.parseInt(st.nextToken());
			
			arr[n2].add(n1);
		}
		
		for (int i = 1; i < n+1; i++) {
			subcount = 0;
			visited = new boolean[n+1];
			dfs(i); // start
			count[i] = subcount;
			max = Math.max(max, subcount);
		}
		
//		for (int i = 0; i < count.length; i++) {
//			System.out.print(count[i] + " ");
//		}
		
		for (int i = 1; i < n+1; i++) {
			if(count[i] == max) {
				sb.append(i).append(" ");
			}
		}
		System.out.print(sb);
	}
	
	
	public static void dfs(int start) {
		visited[start] = true;
		for(int i : arr[start]) {
			if(!visited[i]) {
				subcount += 1;
				
				dfs(i);
			}
		}
	}
	
	
	
}