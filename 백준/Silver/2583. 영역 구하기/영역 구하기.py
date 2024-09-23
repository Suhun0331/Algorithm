'''

'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split()) # 0 2 2 4
    for x in range(x1, x2):
        for y in range(m-y2, m-y1):
            graph[y][x] = 1
            
count = 0
def dfs(x, y):
    global count
    if visited[x][y]:
        return
    visited[x][y] = True
    for i in range(4):
        xx,yy = x + dx[i], y + dy[i]
        if 0<= xx < m and 0<= yy < n and not visited[xx][yy] and graph[xx][yy] == 0:
            count += 1
            
            dfs(xx, yy)
cnt_list = []
summ = 0
for i in range(m):
    for j in range(n):
        count = 1
        if graph[i][j] == 1 or visited[i][j]:
            continue
        dfs(i, j)
        cnt_list.append(count)
        summ += 1

        
cnt_list.sort()
print(summ)
for i in cnt_list:
    print(i, end = ' ')
     