/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.*;
import java.io.*;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	static boolean[][] visited;
	static boolean[] dessert;
	static int answer;
	static int[] dx = {1, 1, -1, -1};
	static int[] dy = {-1, 1, -1, 1};
	static int[][] arr;
	static int n;
	static int count;
	static int starti;
	static int startj;
	static boolean success;
	
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        int T = Integer.parseInt(br.readLine());
        
        for (int t = 0; t < T; t++) {
        	success = false;
        	answer = 0;
			n = Integer.parseInt(br.readLine());
			arr = new int[n][n];
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					visited = new boolean[n][n];
					dessert = new boolean[101];
					count = 0;
					starti = i;
					startj = j;
					dfs(i, j , -1, 0);
					
				}
			}
			
			if(success) {
				sb.append("#").append(t+1).append(" ").append(answer).append("\n");
			}
			else {
				sb.append("#").append(t+1).append(" ").append(-1).append("\n");
			}
		}
        System.out.print(sb);
        
	}
	
	public static void dfs(int ci, int cj, int dir, int turn) {
		visited[ci][cj] = true;
		dessert[arr[ci][cj]] = true;
		count += 1;
		
		for (int i = 0; i < 4; i++) {
			int ni = ci + dx[i];
			int nj = cj + dy[i];
			if(0<=ni && ni < n && 0 <=nj && nj < n) {
				
				int newTurn = turn;
				
				if(dir != -1 && dir != i) {
					newTurn += 1;
				}
				
				if(newTurn > 3) continue;
				
				if(ni == starti && nj == startj && newTurn == 3) {
					success = true;
					answer = Math.max(answer, count);
					return;
				}
				if(!visited[ni][nj] && !dessert[arr[ni][nj]]) {
					dfs(ni, nj, i, newTurn);
					count -= 1;
					visited[ni][nj] = false;
					dessert[arr[ni][nj]] = false;
				}
				
			}
		}
	}
}