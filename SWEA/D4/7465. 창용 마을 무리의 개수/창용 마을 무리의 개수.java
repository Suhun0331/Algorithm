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
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Solution {
	 
    static int n,m;
    static int[] parent;

    static int getParent(int x) {
    	if (parent[x]==x) return x;
    	else return parent[x] = getParent(parent[x]);
    }
    
    static void unionParent(int x, int y) {
      x = getParent(x);
      y = getParent(y);
      
      if(x<y) 
    	  parent[y]=x;
      else 
    	  parent[x]=y;
    }
     
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
     
        int T = Integer.parseInt(br.readLine());
        for(int t=1; t<=T; t++) {
            //input
            int answer=0;
            StringTokenizer tk = new StringTokenizer(br.readLine());
            n = Integer.parseInt(tk.nextToken());
            m = Integer.parseInt(tk.nextToken());
            parent = new int[n+1];
            for(int i=1; i<=n; i++) {
            	parent[i] = i;
            }
            
          //solve
            for(int i=0; i<m; i++) {    
                tk = new StringTokenizer(br.readLine());
                int from = Integer.parseInt(tk.nextToken());
                int to = Integer.parseInt(tk.nextToken());
                unionParent(from,to);
            }
             
            //부모 값이 자기 자신과 같은 것의 개수가 그룹의 개수
            for(int i=1; i<=n;i++) {
            	if(parent[i]==i) {
            		answer++;
            	}
            }
             
            //output
            bw.write("#" + t+ " " + answer +'\n');
        }
        bw.close(); 
    }
}