import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Iterator;
import java.util.Queue;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		
		Queue<Integer> q = new ArrayDeque<>();
		for (int i = 1; i < n+1; i++) {
			q.add(i);
		}
		
		while(q.size() > 1) {
			sb.append(q.poll()).append(" ");
			q.offer(q.poll());
		}
		sb.append(q.poll());
		
		System.out.println(sb);
		
		
	}
}