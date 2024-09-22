n = int(input())

map = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 0

def dfs(i, j):
    global count
    if visited[i][j]:
        return
    visited[i][j] = True
    count += 1
    for k in range(4):
        xx, yy = i+dx[k], j+dy[k]
        if 0<= xx < n and 0<= yy < n and not visited[xx][yy] and map[xx][yy] == 1:
            dfs(xx, yy)
            
cnt = []
sum = 0
for i in range(n):
    for j in range(n):
        if map[i][j] == 0 or visited[i][j]:
            continue
        dfs(i, j)
        cnt.append(count)
        sum += 1
        count = 0

print(sum)
cnt.sort()
for i in cnt:
    print(i)
