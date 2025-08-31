import java.io.*;
import java.util.*;

public class Main {

    static class Node {
        int start, end, weight;
        Node(int s, int e, int w) {
            this.start = s; this.end = e; this.weight = w;
        }
    }

    static int[] parent;

    static void make(int n) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    static int find(int a) {
        if (parent[a] == a) return a;
        return parent[a] = find(parent[a]);
    }

    static boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;
        parent[rb] = ra;
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        while (true) {
            String line = br.readLine();
            if (line == null || line.isEmpty()) break;

            StringTokenizer st = new StringTokenizer(line);
            int n = Integer.parseInt(st.nextToken()); // 정점 수 (0..n-1)
            int m = Integer.parseInt(st.nextToken()); // 간선 수
            if (n == 0 && m == 0) break;

            Node[] edges = new Node[m];
            long total = 0L;

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                int w = Integer.parseInt(st.nextToken());
                edges[i] = new Node(s, e, w);
                total += w;
            }

            Arrays.sort(edges, (a, b) -> Integer.compare(a.weight, b.weight));

            make(n);

            long mst = 0L;
            int picked = 0;
            for (Node edge : edges) {
                if (union(edge.start, edge.end)) {
                    mst += edge.weight;
                    if (++picked == n - 1) break;
                }
            }

            long saving = total - mst;
            out.append(saving).append('\n');
        }

        System.out.print(out);
    }
}
