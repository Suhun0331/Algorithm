import java.util.*;
import java.io.*;

public class Main {
	static int n, m;
	static int[] arr;
	static StringBuilder sb;
	static boolean[] visited;
	public static void main(String[] args) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		sb = new StringBuilder();
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		arr = new int[m];
		visited = new boolean[n+1];
		
		dfs(0);
		
		System.out.println(sb);

		
	}
	
	public static void dfs(int depth) {
		if(depth == m) {
			for(int i = 0; i<m; i++) {
				sb.append(arr[i]).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for(int i = 1; i<=n; i++) {
			if(!visited[i]) {
				arr[depth] = i;
				visited[i] = true;
				dfs(depth+1);
				visited[i] = false;
			}
		}
		
	}
}
