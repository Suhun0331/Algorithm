import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		Stack<Character> stack = new Stack<>();
		StringBuilder sb = new StringBuilder();
		
		
		while(true) {
			String str = br.readLine();
			if (str.equals(".")) break;
			boolean suc = true;
			
			for (int i = 0; i < str.length(); i++) {
				char c = str.charAt(i);
				if(c == '(' || c == '[') {
					stack.add(c);
				}
				else if(c == ')') {
					if(stack.isEmpty()) {
						suc = false; 
						break;
					}
					else if(stack.peek() == '(') stack.pop();
					else if(stack.peek() == '[') {
						suc = false; 
						break;
					}
				}
				else if(c == ']') {
					if(stack.isEmpty()) {
						suc = false; 
						break;
					}
					else if(stack.peek() == '[') stack.pop();
					else if(stack.peek() == '(') {
						suc = false; 
						break;
					}
				}
				
			}
			
			if(!stack.isEmpty()) {
				suc = false;
			}
			if(suc) sb.append("yes").append("\n");
			else sb.append("no").append("\n");
			stack.clear();
		}
		
		
		System.out.print(sb);
		
		
	}

}
