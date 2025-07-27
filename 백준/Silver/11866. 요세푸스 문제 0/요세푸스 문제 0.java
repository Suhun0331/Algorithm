import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Iterator;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		Queue<Integer> q = new ArrayDeque<>();
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		
		for (int i = 1; i < n+1; i++) {
			q.add(i);
		}
		
		while(!q.isEmpty()) {
			for (int i = 1; i < k; i++) {
				q.offer(q.poll());
			}
			sb.append(q.poll());
			if(!q.isEmpty()) {
				sb.append(", ");
			}
			
		}
		
		sb.append(">");
		
		System.out.print(sb);
		
		
	}
}