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
public class Solution {
	
	static class Node{
		int start, end, weight;
		public Node(int start, int end, int weight) {
			super();
			this.start = start;
			this.end = end;
			this.weight = weight;
		}
	}
	
	static int[] parent;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine()); //전체 테케 수
		
		for(int tc=1; tc<=T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int V = Integer.parseInt(st.nextToken()); //정점의 갯수
			int E = Integer.parseInt(st.nextToken()); //간선의 갯수
			
			Node[] edgeList = new Node[E];
			parent = new int[V+1]; //정점 번호가 1부터 시작
			
			for(int i=0; i<E; i++) {
				st = new StringTokenizer(br.readLine());
				int start = Integer.parseInt(st.nextToken());
				int end = Integer.parseInt(st.nextToken());
				int weight = Integer.parseInt(st.nextToken());
				edgeList[i] = new Node(start, end, weight);
			}
			
			Arrays.sort(edgeList, new Comparator<Node>() { //가중치를 기준으로 정렬

				@Override
				public int compare(Node o1, Node o2) {
					return o1.weight - o2.weight;
				}
			});
			
			make(); //각 vertex를 단위 집합으로 만듦
			
			int cnt=0; //선택한 간선의 갯수
			long result=0; //최소신장트리 비용
			
			for(int i=0; i<E; i++) {
				Node edge = edgeList[i];
				if(union(edge.start, edge.end)) { //간선 선택 가능하면
					cnt++;
					result+=edge.weight;
					if(cnt==V-1) { //spanning tree 다 완성됐다면
						break;
					}
				}
			}
			System.out.println("#" + tc + " " + result);
		}
	}

	private static void make() { //서로소 단위집합 만들기
		for(int i=1; i<parent.length; i++) {
			parent[i]=i;
		}
	}
	
	private static int find(int a) {
		
		if(parent[a]==a)
			return a;
		
		return parent[a] = find(parent[a]);
	}
	
	private static boolean union(int a, int b){
		int aRoot = find(a);
		int bRoot = find(b);
		
		if(aRoot==bRoot)
			return false;
		
		parent[bRoot] = aRoot;
		return true;
	}
}