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
import java.util.Scanner;
import java.io.FileInputStream;
import java.util.*;
import java.io.*;

/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
	static int n;
	static int[][] arr;
	static int[] save;
	static int[] notsave;
	static int answer;

	public static void main(String[] args) throws  IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		for (int t = 0; t < T; t++) {
			n = Integer.parseInt(br.readLine());
			answer = Integer.MAX_VALUE;
			arr = new int[n][n];
			save = new int[n/2];
			notsave = new int[n/2];
			
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			dfs(0, 0); // int depth, int start
			
			
			
			sb.append("#").append(t+1).append(" ").append(answer).append("\n");
			
			
		} 
		System.out.print(sb);
		
		
		}
	
	public static void dfs(int depth, int start) {
		if(depth == n/2) {
			int saveidx = 0;
			int notsaveidx = 0;
			for (int i = 0; i < n; i++) {
				if(saveidx < n/2 && save[saveidx] == i) {
					saveidx += 1;
					 
				}
				else {
					notsave[notsaveidx] = i;
					notsaveidx += 1;
				}
			}
			
			int food1 = 0;
			for (int i = 0; i < n/2-1; i++) {
				for (int j = i+1; j < n/2; j++) {
					food1 += (arr[save[i]][save[j]] + arr[save[j]][save[i]]);
				}
			}
			int food2 = 0;
			for (int i = 0; i < n/2-1; i++) {
				for (int j = i+1; j < n/2; j++) {
					food2 += (arr[notsave[i]][notsave[j]] + arr[notsave[j]][notsave[i]]);
				}
			}
			
			answer = Math.min(answer, Math.abs(food1-food2));
			return;
		}
		
		
	
		for (int i = start; i < n; i++) {
			save[depth] = i;
			dfs(depth + 1, i+1);
		}
		
		
		
	}
}