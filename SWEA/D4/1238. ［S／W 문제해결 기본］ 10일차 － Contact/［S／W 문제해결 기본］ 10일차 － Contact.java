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

class Solution
{
	static List<Integer>[] graph;
	
	static boolean[] visited;
	static int answer;
	
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        for (int t = 1; t < 11; t++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int start = Integer.parseInt(st.nextToken());
			
			visited = new boolean[101];
			graph = new ArrayList[101];
			answer = 0;
			for (int i = 1; i < 101; i++) {
				graph[i] = new ArrayList<>();
			}
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n/2; i++) {
				int num1 = Integer.parseInt(st.nextToken());
				int num2 = Integer.parseInt(st.nextToken());
				graph[num1].add(num2); //num1 -> num2
			}
			
			bfs(start);
			
			sb.append("#").append(t).append(" ").append(answer).append("\n");
			
		}
        System.out.print(sb);
        
        
        
    }
	public static void bfs(int start){
    	Queue<Integer> q = new ArrayDeque<>();
    	q.add(start);
    	visited[start] = true;
    	int depth = 0;
    	List<Integer> subarr = new ArrayList<>();
    	
    	while(!q.isEmpty()) {
    		answer = 0;
    		for (int i = 0; i < subarr.size(); i++) {
    			answer = Math.max(answer,  subarr.get(i));
        	}
    		subarr = new ArrayList<>();
    		int size = q.size();
    		
    		for (int i = 0; i < size; i++) {
    			int next = q.poll();
        		for(int n : graph[next]) {
        			if(!visited[n]) {
        				subarr.add(n);
        				visited[n] = true;
        				q.add(n);
        			}
        		}
			}
    		
    	
    	}
    	
    }
}