'''
bfs 사용
1. 익은 토마토 좌표 저장 해놓고 반복문 한 번 돌 때마다 상하좌우 좌표 추가하기

결국 모든 칸 다 확인할 거 아니면 익은 토마토 좌표 저장해놓긴 해야할 듯
좌표 저장 + 상하좌우 한 번 돈 토마토는 좌표에서 삭제 + 토마토 map에는 1 유지
상하좌우 돌 때는 상하좌우에 0이면 1, 1이면 continue, -1이면 pass
익은 토마토 좌표 한 번 다 돌 때마다 day + 1
-> 첫 번째 제출 시간초과 -> sys 추가, 토마토 리스트 말고 deque로 변경 -> 마지막에 틀렸습니다.

'''
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split()) # m = 가로 , n = 세로 -> (n,m)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mapp = []
tomato = deque()
day = 0
count = 0
for i in range(n):
    mapp.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if mapp[i][j] == 1:
            tomato.append((i, j))
        elif mapp[i][j] == -1:
            count += 1
            
if not tomato:
    if count == n*m:
        print(0)
    else:
        print(-1)
    exit()
    
while tomato:
    day += 1
    length = len(tomato)
    for i in range(length):
        nn, mm = tomato.popleft()
        for i in range(4):
            nx, ny = nn+dx[i], mm+dy[i]
            # print(n, m, nx, ny)
            if 0 <= nx < len(mapp) and 0 <= ny < len(mapp[0]):
                if mapp[nx][ny] == 0:
                    mapp[nx][ny] = 1
                    tomato.append((nx,ny))
# for i in mapp:
#     for j in i:
#         print(j, end = ' ')
#     print()
# print()
# print(tomato)
fail = False
for i in range(n):
    # print(n, i)
    # print(mapp[i])
    if 0 in mapp[i]:
        fail = True
        break
# print(fail)
if fail:
    print(-1)
else:
    print(day-1)