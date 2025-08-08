/**
 * 입력 다 받고 1의 친구 array에 저장
 * array 돌면서 이 안에 들어있는 사람들의 친구 수 count + 방문처리
 * 
 */

import java.util.*;
import java.io.*;

public class Main {
	static boolean[] visited;
	static int count;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		
		ArrayList<Integer> arr = new ArrayList<>();
		
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		
		boolean[][] friend = new boolean[n+1][n+1];
		visited = new boolean[n+1];
		count = 0;
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int num1 = Integer.parseInt(st.nextToken());
			int num2 = Integer.parseInt(st.nextToken());
			friend[num1][num2] = true;
			friend[num2][num1] = true; 
		}
		
		
		for (int i = 2; i < n+1; i++) {
			if(friend[1][i]) {
				//어레이에 i 추가 -> i는 1번의 친구
				arr.add(i);
				visited[i] = true;
				count += 1;
			}
		}
		
		for(int i : arr) { // i = 2, 3
			for (int j = 2; j < n+1; j++) {
				if(friend[i][j] && !visited[j] && i != j) {
					visited[j] = true;
//					System.out.println(j);
					count += 1;
				}
			}
		}
		
//		for (int i = 0; i < visited.length; i++) {
//			System.out.print(visited[i] + " ");
//		}
		
		
		System.out.println(count);
	}
	
}