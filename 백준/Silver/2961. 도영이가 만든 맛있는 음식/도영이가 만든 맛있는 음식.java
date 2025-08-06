//백트래킹으로 depth -> 현재 재료 선택 or 선택하지 않음 재귀 2번 반복

import java.util.*;
import java.io.*;

public class Main {
	static int[][] taste;
	static int answer;
	static int n;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());
		taste = new int[n][2];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			taste[i][0] = Integer.parseInt(st.nextToken());
			taste[i][1] = Integer.parseInt(st.nextToken());
		}
		
		if(n == 1) {
			System.out.print(Math.abs(taste[0][1]-taste[0][0]));
			return ;
		}
		
		answer = Math.abs(taste[0][1]-taste[0][0]);
		
		dfs(0, 1, 0, 0);
//		dfs(1, 1, 0);
		
		System.out.println(answer);
		
	}
	
	public static void dfs(int depth, int sour, int bitter, int count) {
		if(depth == n) {
			if(count != 0) {
				answer = Math.min(answer,  Math.abs(sour-bitter));
			}
			return;
		}
		
		dfs(depth+1, sour, bitter, count); // 다음꺼 선택x
		dfs(depth+1, sour*taste[depth][0], bitter+taste[depth][1], count + 1); // 다음꺼 선택 o
		
		
	}
}
