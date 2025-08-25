import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static boolean[] visited;
    static boolean found;

    static void dfs(int v, int depth) {
        if (found) return;          // 이미 조건을 만족했으면 중단
        if (depth == 5) {           // 5명 연결(깊이 5) 달성
            found = true;
            return;
        }
        for (int nxt : graph[v]) {
            if (!visited[nxt]) {
                visited[nxt] = true;
                dfs(nxt, depth + 1);
                visited[nxt] = false;
                if (found) return;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        visited = new boolean[N];
        found = false;

        for (int i = 0; i < N && !found; i++) {
            visited[i] = true;
            dfs(i, 1);
            visited[i] = false;
        }

        System.out.println(found ? 1 : 0);
    }
}
