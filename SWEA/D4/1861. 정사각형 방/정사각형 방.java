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
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int T, N;
	static int [][] A = new int[1000][1000];
	static int [][] D;
	
	static int dr[] = {0,0,1,-1};
	static int dc[] = {1,-1,0,0};

	static int dfs(int r, int c) {
		if (D[r][c] > 0) return D[r][c];
		for (int k=0;k<4;++k) {
			int nr = r + dr[k];
			int nc = c + dc[k];
			if (0<=nr&&nr<N&&0<=nc&&nc<N)
				if (A[nr][nc] == A[r][c] + 1)
					return D[r][c] = dfs(nr,nc) + 1;
		}
		return 0;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		T = Integer.parseInt(br.readLine());
		for (int t=1;t<=T;++t) {
			N = Integer.parseInt(br.readLine());
				
			for (int i=0;i<N;++i) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j=0;j<N;++j)
					A[i][j] = Integer.parseInt(st.nextToken());
			}
			
			D = new int[N][N];
			
			int max = -1, maxRoom = 0;
			for (int i=0;i<N;++i)
				for (int j=0;j<N;++j) {
					int res = dfs(i,j);
					if (res > max || (res==max && A[i][j] < maxRoom)) {
						max = res;
						maxRoom = A[i][j];
					}
				}

			System.out.printf("#%d %d %d\n", t, maxRoom, max+1);
			
		}
	}
}
