'''
위상정렬인건 질문게시판 들어가보고 알았음.
위상정렬 복습

indegree 적은 순으로 탐색하고 지우고 반복 
'''

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    arr = list(map(int, input().split()))
    for j in range(1, arr[0]):
        graph[arr[j]].append(arr[j+1])
        indegree[arr[j+1]] += 1

def sort():
    q = deque()
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    if len(q) == 0:
        print(0)
        return
    while q:
        cur = q.popleft()
        if visited[cur] == True:
            print(0)
            return
        visited[cur] = True
        result.append(cur)
        for i in graph[cur]:
            indegree[i] -= 1

        
            if indegree[i] == 0:
                q.append(i)
    if len(result) != n:
        print(0)
        return
    for i in result:
        print(i)

sort()
