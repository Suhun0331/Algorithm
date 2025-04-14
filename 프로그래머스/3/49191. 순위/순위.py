from collections import deque

def bfs(start, graph, n):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    count = 0

    while q:
        cur = q.popleft()
        for next_node in graph[cur]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                count += 1  # 연결된 노드 수 증가
    return count

def solution(n, results):
    wgraph = [[] for _ in range(n+1)]  # i가 이긴 사람들
    lgraph = [[] for _ in range(n+1)]  # i가 진 사람들

    for win, lose in results:
        wgraph[win].append(lose)
        lgraph[lose].append(win)

    answer = 0
    for i in range(1, n+1):
        win_count = bfs(i, wgraph, n)  # i가 이긴 사람 수
        lose_count = bfs(i, lgraph, n)  # i가 진 사람 수

        if win_count + lose_count == n - 1:
            answer += 1

    return answer
