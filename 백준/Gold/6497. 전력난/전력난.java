import java.util.*;
import java.io.*;

public class Main {
	
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
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken()); //정점의 갯수
			int m = Integer.parseInt(st.nextToken()); //간선의 갯수
			if(n == 0 && m == 0) break;
			
			Node[] edgeList = new Node[m];
			parent = new int[n+1]; //정점 번호가 1부터 시작
			int result = 0;
			
			for(int i=0; i<m; i++) {
				st = new StringTokenizer(br.readLine());
				int start = Integer.parseInt(st.nextToken());
				int end = Integer.parseInt(st.nextToken());
				if(start == 0 && end == 0) break;
				int weight = Integer.parseInt(st.nextToken());
				
				edgeList[i] = new Node(start, end, weight);
				result += weight;
			}
			
			
			Arrays.sort(edgeList, new Comparator<Node>() { //가중치를 기준으로 정렬

				@Override
				public int compare(Node o1, Node o2) {
					return o1.weight - o2.weight;
				}
			});
			
			make(); //각 vertex를 단위 집합으로 만듦
			
			int cnt=0; //선택한 간선의 갯수
			
			for(int i=0; i<m; i++) {
				Node edge = edgeList[i];
				if(union(edge.start, edge.end)) { //간선 선택 가능하면
					cnt++;
					result-=edge.weight;
					if(cnt==n-1) { //spanning tree 다 완성됐다면
						break;
					}
				}
			}
			System.out.println(result);
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