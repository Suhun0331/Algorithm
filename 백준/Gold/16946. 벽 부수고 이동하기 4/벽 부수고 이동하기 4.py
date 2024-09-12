'''
넘 어렵다 ....
아이디어랑 정답 코드는 인터넷 찾아봤고,
한 번 보고 난 뒤 이해하고 코드작성은 혼자서 함.
생각한 방식 코드로 구현하는 연습 했다고 치지 뭐 ,,
마지막 중복 안되게 하려고 set 쓴 것도 기억해두기.
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

map = [list(map(int, input().strip())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
info = {}
zeros = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
group = 1

def bfs(x, y):
    global group
    q.append((x, y))
    count = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        zeros[x][y] = group
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx <= n-1 and 0 <= yy <= m-1:
                if map[xx][yy] == 0 and not visited[xx][yy]:
                    count += 1
                    visited[xx][yy] = True
                    q.append((xx, yy))
                    zeros[xx][yy] = group
    
    return count

for i in range(n):
    for j in range(m):
        cnt = 0
        if map[i][j] == 0 and not visited[i][j]:
            cnt = bfs(i, j)
            
            info[group] = cnt
            group += 1

for i in range(n):
    for j in range(m):
        answer = 1
        data = set()
        if map[i][j] == 1:
            for k in range(4):
                xx = i + dx[k]
                yy = j + dy[k]
                if 0<= xx <= n-1 and 0 <= yy <= m-1:
                    if map[xx][yy] != 1:
                       data.add(zeros[xx][yy])
            
            for add in data:
                answer += info[add]
            print(answer%10, end = '')
        else:
            print(0, end = '')
    print()
