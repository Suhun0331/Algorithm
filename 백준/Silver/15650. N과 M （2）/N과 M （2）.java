
import java.util.*;
import java.io.*;

public class Main {
	static int n;
	static int m;
	static boolean[] visited;
	static int[] arr;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		visited = new boolean[n+1];
		arr = new int[m+1];
		
		dfs(1, 0);
		
		System.out.print(sb);
		
		
	}
	public static void dfs(int start, int depth) {
		if(depth == m) {
			for (int i = 0; i < m; i++) {
				sb.append(arr[i]).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i = start; i <= n; i++) {
			if(!visited[i]) {
				visited[i] = true;
				arr[depth] = i;
				dfs(i, depth+1);
				visited[i] = false;
			}
		}
		
		
	}
	
	
	
	
}
