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

public class Solution {
    static int N;
    static int [][] arr;
    static int maxDepth;
    static boolean [][] visited;
    static int [] dx = {1, 0, -1, 0};
    static int [] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            // 입력
            N = Integer.parseInt(br.readLine());
            arr = new int [N][N];
            for (int i = 0; i < N; i++) {
                String [] s = br.readLine().split(" ");
                for (int j = 0; j < N; j++) {
                    arr[i][j] = Integer.parseInt(s[j]);
                }
            }

            // 초기화
            int answer = 0;
            int startPoint = 0;
            visited = new boolean [N][N];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j]) {
                        maxDepth = 0;
                        dfs(i, j, 1); // i, j가 추가되었으므로 depth는 1부터 시작
                        if (maxDepth == answer)
                            startPoint = Math.min(startPoint, arr[i][j]); // 여러개 가능하면 값이 더 작은 쪽으로
                        else if (maxDepth > answer) {
                            answer = maxDepth; // answer 갱신
                            startPoint = arr[i][j];
                        }
                    }
                }
            }
            System.out.println("#" + tc + " " + startPoint + " " + answer);
        }
    }
    
    public static void dfs(int x, int y, int depth) {
        maxDepth = Math.max(depth, maxDepth);

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (!(0 <= nx && nx < N && 0 <= ny && ny < N))
                continue;
            
            if (visited[nx][ny])
                continue;
            
            if (arr[nx][ny] == arr[x][y] + 1)
                dfs(nx, ny, depth + 1);
        }
    }
}
