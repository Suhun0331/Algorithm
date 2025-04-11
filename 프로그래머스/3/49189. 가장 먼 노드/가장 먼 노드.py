'''
그래프탐색 -> 유니온 파인드 / 위상정렬
유니온파인드 -> 방향 없는 그래프 탐색 (ex 사이클 판별)
위상정렬 -> 사이클 없는 방향 있는 그래프 탐색

1번노드에서 시작해서 뻗어나가니까 bfs / dfs?
visited 사용해서 뻗어나가면 될 듯, 근데 bfs가 편할 듯 함 -> q 사용

뻗어나가다가 더이상 갈 곳이 없으면 지금까지 지나온 간선 개수 리스트에 저장
마지막에는 count(max(카운트 리스트))로 값 반환

---
다른 사람 풀이 중엔 내 코드가 속도 제일 빠른 듯 + 코드 최적화 
'''
from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    visited = [False] * (n+1)
    visitcount = [0] * (n+1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque([1])
    visited[1] = True
        
    while q:
        cur = q.popleft()
        visited[cur] = True
        
        for i in graph[cur]:
            if not visited[i]: # 아직 방문 안한 노드라면
                visited[i] = True
                q.append(i)
                visitcount[i] = visitcount[cur] + 1
                
            
    return visitcount.count(max(visitcount))
