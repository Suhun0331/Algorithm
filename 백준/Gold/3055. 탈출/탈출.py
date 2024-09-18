'''
역대급 시간 많이 쓴 문제;
첨엔 문제 이해 잘못해서 시간 날리고
그 뒤에 내 방식대로 구현 하려다가 문제 못 찾아서 또 시간 날림
결국 인터넷 풀이 썼다 하ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ

근데 bfs 한 번만 써도 되는데 다들 2개로 나눠서 쓰라네?
'''

import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

map = [list(map(str, input().strip())) for i in range(r)]

start = []
end = []
water = []
q = deque()
for i in range(r):
    for j in range(c):
        if map[i][j] == 'D':
            end.append([i, j])
        if map[i][j] == 'S':
            start.append([i,j])
            q.append([i, j])


for i in range(r):
    for j in range(c):    
        if map[i][j] == '*':
            water.append([i,j])
            q.append([i, j])


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[-1]*c for i in range(r)]
visited[start[0][0]][start[0][1]] = 0
#print(visited)

while q:
    x, y = q.popleft()
    
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= r or yy < 0 or yy >= c:
            continue
        if map[x][y] == 'S' and (map[xx][yy] == '.' or map[xx][yy] == 'D'):
            if map[xx][yy] == 'D':
                print(visited[x][y] + 1)
                sys.exit()
            map[xx][yy] = 'S'
            visited[xx][yy] = visited[x][y] + 1
            q.append([xx, yy])
            #print(q)
            
        elif map[x][y] == '*' and (map[xx][yy] == '.' or map[xx][yy] == 'S'):
            map[xx][yy] = '*'
            q.append([xx, yy])

    
    #print(map)


if visited[end[0][0]][end[0][1]] == -1:
    print('KAKTUS')
else:
    print(visited[end[0][0]][end[0][1]])
