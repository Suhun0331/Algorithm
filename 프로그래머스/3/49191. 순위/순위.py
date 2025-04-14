'''
3이 4를 이김 -> 3은 4가 이긴 사람들 또한 이긴 것
3이 4한테 짐 -> 3은 4가 진 사람들한테도 진 것

그냥 순서대로 그래프 타고 갔을 때 모든 사람과 이어져있으면 되는 거 아닌가? 아님.

2를 생각해봤을 때, 2를 기준으로 뻗어져 나간 번호 + 2에 들어온 사람 번호 합쳤을 때
모두 방문 되는거면 ok
5 또한 5에서 뻗어져 나갔을 때 모두에게 도달함.

근데 만약 2로 들어온 애들을 탐색한다면, 계속 같은 방향이어야 함.
2로 들어온 노드 탐색 -> 그 노드로 들어온 노드 탐색 . . .
나가는 것도 마찬가지로 2에서 나간 3 -> 3에서 나간 4
이런 식으로 나감 / 들어옴 방향을 일치 시켜서 전체 탐색 했을 때 모두에게 닿으면 ok

이긴 관계 그래프, 진 관계 그래프 두개 만들기? -> 시간 초과 
문제 이유 : visited가 제대로 이뤄지지 않았었음.
함수화 + visited 제대로 처리한 후 리팩토링

플로이드 워셜로 푼 사람이 많은데, 그럼 n^3 -> 이 방법이 훨씬 빠름.
'''
from collections import deque

def solution(n, results):
    answer = 0
    wgraph = [[] for _ in range(n+1)]
    lgraph = [[] for _ in range(n+1)]
    for a, b in results:
        wgraph[a].append(b) # wgraph[a] -> a가 이긴 애들
        lgraph[b].append(a) # lgraph[b] -> b가 진 애들

    def bfs(start, graph):
        visited = [False] * (n+1)
        visited[start] = True
        count = 0
        q = deque([start])
        while q:
            cur = q.popleft()
            for k in graph[cur]:
                if not visited[k]:
                    q.append(k)
                    visited[k] = True
                    count += 1
        return count
    
    final = 0
    for i in range(1, n+1):
        answer = 0
        answer += bfs(i, wgraph)
        answer += bfs(i, lgraph)
                    
        if answer == n-1:
            final += 1


    return final