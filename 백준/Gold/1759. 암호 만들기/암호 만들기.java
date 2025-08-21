import java.io.*;
import java.util.*;
public class Main {
	static List<Character> answer;
	static char[] arr;
	static StringBuilder sb;
	static int l;
	static int c;
	
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        sb = new StringBuilder();
        
        st = new StringTokenizer(br.readLine());
        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        
        arr = new char[c];
        
        for (int i = 0; i < c; i++) {
			arr[i] = st.nextToken().charAt(0);
		}
        
        
        answer = new ArrayList<>();
        Arrays.sort(arr);
        
        for (int i = 0; i <= c-l; i++) {
        	answer = new ArrayList<>();
        	answer.add(arr[i]);
        	if(arr[i] == 'a' || arr[i] == 'e' ||arr[i] == 'i' ||arr[i] == 'o' ||arr[i] == 'u') dfs(i, 0, 1);
        	else dfs(i, 1, 0);
			
		}
        
        System.out.print(sb);
        
        
	}
	
	public static void dfs(int start, int ja, int mo) {
		if(answer.size() == l) {
			if(ja >= 2 && mo >= 1) {
				for (int i = 0; i < answer.size(); i++) {
					sb.append(answer.get(i));
				}
				sb.append("\n");
				return;
			}
			else return;
		}
		
		for (int i = start+1; i < c; i++) {
			if(arr[i] == 'a' || arr[i] == 'e' ||arr[i] == 'i' ||arr[i] == 'o' ||arr[i] == 'u') {
				answer.add(arr[i]);
				dfs(i, ja, mo+1);
				answer.remove(answer.size() - 1);
			}
			else {
				answer.add(arr[i]);
				dfs(i, ja+1, mo);
				answer.remove(answer.size() - 1);
			}
			
		}
		
	}
}