'''
처음에 엄청난 하드코딩 조지다가 이건 아니다 싶어서
moves로 이동 배열 만듦
중복 코드가 좀 많은 거 같다
최적화 하는 방법 찾아봐야지
'''
from collections import deque

n = int(input())

a, b, c, d = map(int, input().split())

start = [a, b]
end = [c, d]
queue = deque()

visit = [[False for i in range(n)] for i in range(n)]
moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
move_count = [[0 for i in range(n)] for i in range(n)]

visit[a][b] = True
queue.append((a,b))
finish = False

while queue:
    r, c = queue.popleft()
    #print(r, c)
    for move in moves:
        x = r + move[0]
        y = c + move[1]
        if x<0 or x>n-1 or y<0 or y>n-1 or visit[x][y] == True:
            continue
        
        visit[x][y] = True
        queue.append((x, y))
        move_count[x][y] = move_count[r][c] + 1
        
    #print(queue)

    if move_count[end[0]][end[1]] != 0:
        break


if move_count[end[0]][end[1]] != 0:
    print(move_count[end[0]][end[1]])
else:
    print(-1)

