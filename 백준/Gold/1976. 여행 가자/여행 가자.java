import java.util.*;
import java.io.*;

public class Main {

	static int[] parents;
	static int answer;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine()); // 사람 수
		int M = Integer.parseInt(br.readLine()); // 관계 수

		answer = 0;
		parents = new int[N + 1];
		for (int i = 1; i < parents.length; i++) {
			parents[i] = i;
		}

		for (int i = 1; i < N+1; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j < N+1; j++) {
				int sub = Integer.parseInt(st.nextToken());
				if(sub == 1) {
					union(i, j);
				}
			}

		}

		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		boolean check = true;
		for (int i = 1; i < M; i++) {
			int next = Integer.parseInt(st.nextToken());
			if(find(next) == find(start)) {
				continue;
			}
			else {
				check = false;
				break;
			}
		}
		
		if(check) {
			System.out.println("YES");
		}
		else {
			System.out.println("NO");
		}

		
	}
    
    	private static void union(int a, int b) {
		int pa = find(a);
		int pb = find(b);

		if (pa != pb) {
			parents[pa] = pb;
		}

	}

	private static int find(int a) {
		if (parents[a] == a) {
			return a;
		} else {
			return parents[a] = find(parents[a]);
		}

	}

}