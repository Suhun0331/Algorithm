import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def dfs(x, y):
    visited[x][y] = True
    for i in range(8):
        xx, yy = x + dx[i], y + dy[i]
        if 0<= xx < h and 0<= yy < w and not visited[xx][yy] and graph[xx][yy] == 1:
            dfs(xx, yy)
    
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if visited[i][j] or graph[i][j] == 0:
                continue
            dfs(i, j)
            count += 1
    print(count)


