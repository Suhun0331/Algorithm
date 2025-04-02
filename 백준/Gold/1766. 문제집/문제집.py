'''
위상정렬 + 우선순위 큐

먼저 입력 받은 값 위상정렬 테이블 만들기
처음에 root 뽑힐텐데 그거 우선순위 큐에 넣음
heapq.heappop으로 뽑아서 위상정렬 업데이트 하고, 업데이트 된 값 다시 우선순위 큐에 넣기.
그냥 위상정렬 문제를 큐가 아니라 우선순위 큐에 넣는걸로만 바꾸면 될 듯 
'''
import heapq as hq
q = []
hq.heapify(q)
n, m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
answer = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        hq.heappush(q, i)

while q:
    cur = hq.heappop(q)
    answer.append(cur)
    for i in graph[cur]:
        indegree[i] -= 1
        if indegree[i] == 0:
            hq.heappush(q, i)

for i in answer:
    print(i, end = ' ')


