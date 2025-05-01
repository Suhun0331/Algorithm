'''
bfs
6방향 모두 탐색
'''
import sys
from collections import deque
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split()) #m:가로, n:세로, h:높이(h, n, m)
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
#print(visited)
tomato = []
q = deque()
count = 0
for j in range(h):
    tomato_sub = []
    for i in range(n):
        line = list(map(int, input().split()))
        tomato_sub.append(line)
    tomato.append(tomato_sub)
check = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                check += 1

if check == 0:
    print(0)
    exit()


for i in range(h):
    for j in range(n):
        for k in range(m):
            #print(i, j, k)
            if tomato[i][j][k] == 1:
                visited[i][j][k] = True
                q.append((i, j, k))
    
#m:가로, n:세로, h:높이(h, n, m)
def bfs():
    global count
    while q:
        count += 1
        length = len(q)
        for i in range(length):
            ch, cn, cm = q.popleft()
            for i in range(6):
                nh, nn, nm = ch+dx[i], cn+dy[i] , cm+dz[i]
                if 0<=nh<h and 0<=nn<n and 0<=nm<m:
                    if not visited[nh][nn][nm] and tomato[nh][nn][nm] == 0:
                        tomato[nh][nn][nm] = 1
                        q.append((nh, nn, nm))

bfs()
    
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] != 0:
                continue
            else:
                print(-1)
                exit()
print(count-1)
