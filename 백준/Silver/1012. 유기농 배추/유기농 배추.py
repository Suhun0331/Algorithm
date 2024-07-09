import sys
sys.setrecursionlimit(10 ** 6)

case = int(input())

def dfs(x, y):
    if x<0 or x>=col or y<0 or y>=row:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for _ in range(case):
    col, row, baechu = map(int, input().split())
    graph = []
    for i in range(row):
        graph.append([0]*col)
    for i in range(baechu):
        a, b = map(int, input().split())
        graph[b][a] = 1

        
    result = 0
    for i in range(row):
        for j in range(col):
            if dfs(j, i) == True:
                result += 1
    print(result)
