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
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		Queue<Integer> q = new ArrayDeque<>();
		int last = 0;
		
		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			String str = st.nextToken();
			
			
			if(str.equals("push")) {
				int num = Integer.parseInt(st.nextToken());
				q.add(num); 
				last = num;
			}
			else if(str.equals("front")) {
				if(q.isEmpty()) sb.append(-1).append("\n");
				else sb.append(q.peek()).append("\n");
			}
			else if(str.equals("back")) {
				if(q.isEmpty()) sb.append(-1).append("\n");
				else sb.append(last).append("\n");
			}
			else if(str.equals("size")) sb.append(q.size()).append("\n");
			else if(str.equals("pop")) {
				if(q.isEmpty()) sb.append(-1).append("\n");
				else sb.append(q.poll()).append("\n");
			}
			else if(str.equals("empty")) {
				if(q.isEmpty()) sb.append(1).append("\n");
				else sb.append(0).append("\n");
			}
			
		}
		
		System.out.print(sb.toString());
		
		
	}
}