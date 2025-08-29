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
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			char[][] map = new char[n][m];
			boolean[][] visited = new boolean[n][m];
			
			Queue<int[]> su = new ArrayDeque<>();
			Queue<int[]> devil = new ArrayDeque<>();
			int day = 0;
			boolean check = false;
			
			for (int i = 0; i < n; i++) {
				String str = br.readLine();
				for (int j = 0; j < m; j++) {
					map[i][j] = str.charAt(j);
					if(map[i][j] == '*') {
						devil.add(new int[] {i, j});
					}
					else if(map[i][j] == 'S') {
						su.add(new int[] {i, j});
					}
				}
				
			}
			
			while(!su.isEmpty()) {
				int devilsize = devil.size();
				for (int i = 0; i < devilsize; i++) {
					int[] sub = devil.poll();
					int cn = sub[0];
					int cm = sub[1];
					for (int j = 0; j < 4; j++) {
						int nn = cn + dx[j];
						int nm = cm + dy[j];
						if(0<=nn && nn < n && 0<= nm && nm < m) {
							if(map[nn][nm] != 'X' && map[nn][nm] != 'D' && map[nn][nm] != '*') {
								devil.add(new int[] {nn, nm});
								map[nn][nm] = '*';
							}
						}
					}
				}
				
//				for (int i = 0; i < n; i++) {
//					for (int j = 0; j < m; j++) {
//						System.out.print(map[i][j]);
//					}
//					System.out.println();
//				}
//				System.out.println();
				
				int susize = su.size();
				for (int i = 0; i < susize; i++) {
					int[] sub = su.poll();
					int cn = sub[0];
					int cm = sub[1];
					for (int j = 0; j < 4; j++) {
						int nn = cn + dx[j];
						int nm = cm + dy[j];
						if(0<=nn && nn < n && 0<= nm && nm < m) {
							if(map[nn][nm] != 'X' && map[nn][nm] != '*' && !visited[nn][nm]) {
								if(map[nn][nm] == 'D') {
									check = true;
									break;
								}
								visited[nn][nm] = true;
								su.add(new int[] {nn, nm});
								map[nn][nm] = 'S';
							}
						}
					}
					if(check) break;
					
				}
				
				if(check) break;
				day += 1;
				
				
			}
			
			if(!check) {
				sb.append("#").append(t+1).append(" ").append("GAME OVER").append("\n");
			}
			else {
				sb.append("#").append(t+1).append(" ").append(day+1).append("\n");
			}
			
		}
		System.out.print(sb);
		
		
	}
}