'''
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 칸 중 청소되지 않은 빈 칸이 없는 경우,
    2A. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2B. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 칸 중 청소되지 않은 빈 칸이 있는 경우, 회전한다.
    3B. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3C. 1번으로 돌아간다.
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split()) #(r, c), (n, m)
dx = [-1, 0, 1, 0] #(x, y)
dy = [0, 1, 0, -1]
count = 0
room = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    room.append(list(map(int, input().split())))

def in_range(r, c):
    if 0 <= r < n and 0 <= c < m:
        return True
    else:
        return False
        
def solve(cr, cc, d):
    global count
    while True:
        if room[cr][cc] == 0:
            count += 1
            room[cr][cc] = 2 # 청소한 방 = 2
            
        for _ in range(4):
            d = (d-1)%4
            nr, nc = cr + dx[d], cc + dy[d]
            if room[nr][nc] == 0:
                cr, cc = nr, nc
                #d = (d-1)%4
                break
        else: # 4방향 모두 확인 결과 청소 안된 곳 없음
            
            if room[cr+dx[(d+2)%4]][cc+dy[(d+2)%4]] == 1: #뒷 방향 확인
                print(count)
                return
            else:
                cr, cc = cr+dx[(d+2)%4], cc+dy[(d+2)%4]
            
solve(r, c, d)