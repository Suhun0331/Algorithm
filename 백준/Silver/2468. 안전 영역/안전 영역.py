import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]

a, b = min(map), max(map)
minn, maxx = min(a), max(b)
#print(maxx)
#print(minn)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[False]*n for _ in range(n)]

def dfs(x, y, high):
    if visited[x][y]:
        return
    visited[x][y] = True
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0<= xx < n and 0<=yy<n and map[xx][yy] >= high and not visited[xx][yy]:
            dfs(xx, yy, high)
count = 0
answer = 1
for h in range(1, 101):
    count = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] or map[i][j] < h:
                continue
            dfs(i, j, h)
            count += 1
    answer = max(answer, count)
            

print(answer)
