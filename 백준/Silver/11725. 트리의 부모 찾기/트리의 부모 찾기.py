'''

'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [[] for _ in range(n+1)]

def dfs(node):
    global parent
    if visited[node]:
        return
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            parent[i] = node
        dfs(i)

dfs(1)
for i in range(2, n+1):
    print(parent[i])

    

