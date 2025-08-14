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
import java.io.*;
import java.util.*;

class Solution {
	static int arr[][];
	static int dp[][];
	static int dr[] = { 0, 0, -1, 1 };
	static int dc[] = { -1, 1, 0, 0 };

	static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());

		for (int test_case = 1; test_case <= T; test_case++) {
			N = Integer.parseInt(br.readLine());
			arr = new int[N][N];
			dp = new int[N][N];

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			int startNum = Integer.MAX_VALUE;
			int max = Integer.MIN_VALUE;

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (dp[i][j] == 0)
						dfs(i, j);
				}
			}

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (max < dp[i][j]) {
						startNum = arr[i][j];
						max = dp[i][j];
					} else if (max == dp[i][j]&& startNum > arr[i][j]) {
						startNum = arr[i][j];
						max = dp[i][j];
					}
				}
			}

			sb.append("#" + test_case + " " + startNum + " " + max + "\n");
		}
		System.out.println(sb);
	}

	public static int dfs(int row, int col) {
		if (dp[row][col] != 0)
			return dp[row][col];

		dp[row][col] = 1;

		for (int i = 0; i < 4; i++) {
			int nr = row + dr[i];
			int nc = col + dc[i];

			if (nr < 0 || nr >= N || nc < 0 || nc >= N)
				continue;

			if (arr[row][col] + 1 == arr[nr][nc]) {
				dp[row][col] = Math.max(dp[row][col], dfs(nr, nc) + 1);
			}
		}
		return dp[row][col];
	}

}
