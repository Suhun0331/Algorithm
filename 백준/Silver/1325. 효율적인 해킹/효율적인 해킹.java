/**
 * 중간지점 컴퓨터는 답이 될 수 x, 시작지점 컴퓨터만 확인
 * 타고 들어가면서 visited 처리 -> 중간 컴퓨터는 확인 안하고 pass 가능
 * 배열 하나 만들어서 컴퓨터 번호당 이어진 컴퓨터 개수 저장, 최대 count와 일치하는 컴퓨터 번호 출력
 * 
 */

import java.util.*;
import java.io.*;

public class Main {
	static boolean[] visited;
	static ArrayList<Integer>[] arr;
	static int count;
	static int max;
	static int[] countarr;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		arr = new ArrayList[n+1];
		for(int i = 0; i<n+1; i++) {
			arr[i] = new ArrayList<Integer>();
		}
		visited = new boolean[n+1];
		count = 0;
		max = 0;
		countarr = new int[n+1];
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			arr[b].add(a);
		}
		
		for (int i = 1; i < n+1; i++) {
			count = 0;
			visited = new boolean[n+1];
			dfs(i);
			countarr[i] = count;
			max = Math.max(max, count);
			
		}
		
		for (int i = 1; i < n+1; i++) {
			if(countarr[i] == max) {
				sb.append(i).append(" ");
			}
		}
		
		
		System.out.print(sb);
	}
	
	public static void dfs(int num) {
		visited[num] = true;
		for(int i : arr[num]) {
			if(!visited[i]) {
				count += 1;
				dfs(i);
			}
		}
		
	}
	
}
