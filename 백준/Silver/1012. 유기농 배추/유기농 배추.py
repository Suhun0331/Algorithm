import sys
sys.setrecursionlimit(10 ** 6)
t = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#(n, m) -> (y, x)
count = 0
def dfs(x, y):
    visited[y][x] = True
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<= xx < m and 0 <= yy < n and not visited[yy][xx] and arr[yy][xx] == 1:
            dfs(xx, yy)

for _ in range(t):
    count = 0
    m, n, k = map(int, input().split())

    arr = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and arr[i][j] == 1:
                dfs(j, i)
                count += 1
    print(count)

