'''
처음에 떠올린 아이디어대로 코드 작성
제발 이 방법 맞길 ..
'''

import sys
from collections import deque
input = sys.stdin.readline

arr = []
for i in range(8):
    arr.append(list(map(str, input().strip())))

wall = []

for i in range(8):
    for j in range(8):
        if arr[i][j] == '#':
            wall.append([i,j])

dx = [1, -1, 0, 0, 1, 1, -1, -1, 0]
dy = [0, 0, 1, -1, 1, -1, 1, -1, 0]
q = deque()
q.append([7,0])
time = 0

while q:
    visited = [[False]*8 for _ in range(8)]
    #print(q)
    if time >= 9:
        print(1)
        break
    for _ in range(len(q)):
        x, y = q.popleft()

        if [x, y] in wall:
            continue
        
        for i in dx:
            for j in dy:
                xx = x+i
                yy = y+j
                if 0<= xx <= 7 and 0 <= yy <= 7 and visited[xx][yy] == False:
                    if [xx, yy] not in wall:
                        q.append([xx, yy])
                        visited[xx][yy] = True
                        
    for i in range(len(wall)):
        wall[i] = [wall[i][0]+1, wall[i][1]]
            
    time += 1
    #print(time)
    
if time != 9:
    print(0)