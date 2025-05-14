'''
dfs로 깊이 4까지 들어가기 - visit 처리하면 모든 경우의 수 다 나올 듯
앞에서부터 다 돌면서 최댓값 저장

dfs 쓰면 안됨 -> ㅗ 모양 처리 못함. 얘만 따로 처리 해도 될 듯 

1차 제출 -> 시간초과 -> 매 반복마다 visited 만들지 말고 그냥 재사용

-----
가지치기 코드 추가
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

table = []
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    table.append(list(map(int, input().split())))
max_val = max(map(max, table))
    
def dfs(n, m, visited, sum, count): # (n, m)
    global answer

    if sum + (max_val * (4 - count)) <= answer:
        return
        
    if count == 4:
        answer = max(answer, sum)
        return
    visited[n][m] = True
    for i in range(4):
        nx, ny = n + dx[i], m + dy[i]
        if 0 <= nx < len(table) and 0<= ny < len(table[0]) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, visited, sum+table[nx][ny], count+1)
            visited[nx][ny] = False
    
def check_other(n, m):
    global answer
    dir = [[(0, 1), (0, -1), (1, 0)],
     [(0, 1), (0, -1), (-1, 0)],
     [(1, 0), (-1, 0), (0, -1)],
     [(1, 0), (-1, 0), (0, 1)]]

    for i in dir:
        summ = table[n][m]
        for j in i:
            nx, ny = n + j[0], m + j[1]
            if 0 <= nx < len(table) and 0<= ny < len(table[0]):
                summ += table[nx][ny]
            else:
                break
        answer = max(answer, summ)
    
for i in range(n):
    for j in range(m):
        dfs(i, j, visited, table[i][j], 1)
        check_other(i, j)
        visited[i][j] = False
print(answer)
    