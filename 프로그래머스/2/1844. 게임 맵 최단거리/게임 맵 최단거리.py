import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append([0,0])
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    count[0][0] = 1
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        if x == (n-1) and y == (m-1):
            print(count[x][y])
            return count[x][y]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy] and maps[xx][yy] == 1:
                
                q.append([xx, yy])
                count[xx][yy] = count[x][y] + 1
                visited[xx][yy] = True
    return -1