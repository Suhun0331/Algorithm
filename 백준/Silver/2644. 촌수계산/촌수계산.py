'''
처음 아이디어 생각하는데 조금 시간 걸리긴 했는데
구현 자체는 어렵지 않았던 듯 
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
target1, target2 = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

m = int(input())


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

sum_arr = [0]*(n+1)
def dfs(node):
    global sum_arr
    if visited[node]:
        return
    visited[node] = True
    if node == target2:
        print(sum_arr[node])
        sys.exit()
    for i in graph[node]:
        if visited[i]:
            continue
        sum_arr[i] = sum_arr[node] + 1
        dfs(i)

dfs(target1)

print(-1)
       