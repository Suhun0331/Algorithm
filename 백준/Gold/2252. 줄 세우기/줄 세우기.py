'''
첫 위상정렬 문제, 인터넷 코드 보면서 따라해본거. 다음에 다시 풀어보기
'''
import sys
from collections import deque

input = sys.stdin.readline

v, e = map(int, input().split())

indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
answer = []

for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    answer.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in answer:
    print(i, end = ' ')


                
    
