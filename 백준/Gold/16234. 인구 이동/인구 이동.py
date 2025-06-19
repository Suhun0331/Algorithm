'''
bfs
시작점부터 뻗어나가면서 경계선 열 수 있으면 이동 + visited 업데이트
bfs 진행하는동안 인원수 다 누적합하고 bfs 끝나면 //n 해서 인원 분배

전체 bfs 한 번 다 돌면 answer += 1 하고 visited 초기화하고 반복.
'''
from collections import deque

n, l, r = map(int, input().split())

rand = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
day = 0
for _ in range(n):
    rand.append(list(map(int, input().split())))

def bfs(row, col, visited):
    global check
    q = deque()
    q.append((row, col))
    people = rand[row][col]
    visited[row][col] = True
    save_posi = [(row, col)]
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr+dx[i], cc+dy[i]
            if 0<= nr < len(rand) and 0 <= nc < len(rand[0]) and not visited[nr][nc]:
                #print(abs(rand[cr][cc] - rand[nr][nc]), l, r)
                if l <= abs(rand[cr][cc] - rand[nr][nc]) <= r:
                    #print('check')
                    check = True
                    save_posi.append((nr, nc))
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    people += rand[nr][nc]
                    
    for row, col in save_posi:
        rand[row][col] = people//len(save_posi)
        
while True:
    visited = [[False]*n for _ in range(n)]
    
    check = False
    for row in range(n):
        for col in range(n): 
            if not visited[row][col]:
                bfs(row, col, visited)
    if check:
        day += 1
    else:
        print(day)
        break