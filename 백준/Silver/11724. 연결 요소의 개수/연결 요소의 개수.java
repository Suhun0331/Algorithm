// 양방향 노드 연결 -> 반복문 돌면서 1번 노드부터 확인, visited 사용해서 true면 패스

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import java.io.*;

public class Main {
	
	static List<Integer>[] arr;
	static boolean[] visited;
	static int count;

	public static void main(String[] args) throws FileNotFoundException , IOException {
//		System.setIn(new FileInputStream("Test3.txt"));
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		st = new  StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		visited = new boolean[n+1];
		
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
	
		for (int i = 1; i < n+1; i++) {
			if(!visited[i]) {
				dfs(i);
				count += 1;
		}
		
	}
		System.out.println(count);

	}
	
	public static void dfs(int start) { // 01 , 1 2, 2 3 ,
			
			
			for (int i : arr[start]) {
				if(!visited[i]) {
					visited[i] = true;
					dfs(i);
				}
			}
			
			
		}

}

// 1 - 2 - 3    4 - 5   6