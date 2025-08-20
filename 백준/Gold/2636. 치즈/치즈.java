import java.io.*;
import java.util.*;


public class Main {
	static boolean[][] visited;
	static int answer;
	static Queue<int[]> q;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, -1, 0, 1};
	static int[][] arr;
	static int time;
	
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        
        st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        
        int[][] arr = new int[h][w];
        int count = 0;
        
        for (int i = 0; i < h; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < w; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
        
        q = new ArrayDeque<>();
        int background = -1;
        
        while(background != 0) {
        	visited = new boolean[h][w];
        	q.add(new int[] {0, 0});
        	visited[0][0] = true;
        	count = 0;
        	background = 1;
        	while(!q.isEmpty()) {
        		int[] sub = q.poll();
        		int ci = sub[0];
        		int cj = sub[1];
        		
        		for (int i = 0; i < 4; i++) {
					int ni = ci + dx[i];
					int nj = cj + dy[i];
					if(0<=ni && ni<h && 0<=nj && nj<w && !visited[ni][nj]) {
						if(arr[ni][nj] == 0) {
							visited[ni][nj] = true;
							q.add(new int[] {ni, nj});
							background += 1;
						}
						else {
							count += 1;
							visited[ni][nj] = true;
							arr[ni][nj] = 0;
						}
					}
				}
        		
        	}
        	if(background == h*w) break;
        	time += 1;
        	answer = count;
        	
        }
        
        System.out.println(time);
        System.out.println(answer);
        
        
        
        
	}
}