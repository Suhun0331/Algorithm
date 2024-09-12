'''
기존 방식처럼 그냥 2차원 visited 써서 풀면 될 줄 알았음
n이랑 m이 둘다 1000이라서 시간복잡도 계산하면 1조 -> 브루트포스 불가능
3차원 배열 생각도 못함 .. 인터넷 찾아보고도 이해하는데 시간 걸림
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()

def bfs():
    global visited
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        x, y, crash = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][crash]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx <= n-1 and 0 <= yy <= m-1:
                if map[xx][yy] == 0 and visited[xx][yy][crash] == 0:
                    q.append((xx, yy, crash))
                    visited[xx][yy][crash] = visited[x][y][crash] + 1
                elif map[xx][yy] == 1 and  visited[xx][yy][crash] == 0:
                    if crash == 1:
                        continue
                    else:
                        q.append((xx, yy, 1))
                        visited[xx][yy][1] = visited[x][y][crash] + 1
    return -1
#print(visited)

print(bfs())
                    
