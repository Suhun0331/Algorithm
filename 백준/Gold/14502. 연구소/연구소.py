'''
아이디어가 아예 안떠올라서 찾아봄
bfs + 백트래킹인거 알고 다시 문제풀이 시작
'''

from collections import deque
import sys
input = sys.stdin.readline
import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for j in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

def bfs():
    count = 0
    queue = deque()
    subarr = copy.deepcopy(arr)
    
    for i in range(n):
        for j in range(m):
            if subarr[i][j] == 2:
                queue.append((i, j))
                
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            if 0<= i+dx[k] <= n-1 and 0<= j+dy[k] <= m-1:
                if subarr[i+dx[k]][j+dy[k]] == 0:
                    subarr[i+dx[k]][j+dy[k]] = 2
                    #count += 1
                    queue.append((i+dx[k],j+dy[k]))
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if subarr[i][j] == 0:
                safe_area += 1
                
                    

    #return count
    return safe_area


def createWall(wall_cnt):
    global result
    if wall_cnt == 3:
        result = max(result, bfs())
        return
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 0:
                arr[x][y] = 1
                createWall(wall_cnt + 1)
                arr[x][y] = 0 

        

createWall(0)

print(result)
