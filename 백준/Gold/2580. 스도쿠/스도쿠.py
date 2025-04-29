import sys
input = sys.stdin.readline

def rowcheck(row, num):
    if num in arr[row]:
        return False
    else:
        return True

def colcheck(col, num):
    for i in range(9):
        if arr[i][col] == num:
            return False
    return True

def squcheck(row, col, num):
    r, c = row//3*3, col//3*3
    for i in range(3):
        for j in range(3):
            if arr[r+i][c+j] == num:
                return False
    return True
            
arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

pos = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            pos.append((i,j))

dep = 0
def dfs(r, c, dep):
    if dep == len(pos):
        for i in arr:
            for j in i:
                print(j, end = ' ')
            print()
        exit()
    r, c = pos[dep]
    for i in range(1, 10):
        if rowcheck(r, i) and colcheck(c, i) and squcheck(r, c, i):
            arr[r][c] = i
            #dep += 1
            dfs(r, c, dep+1)
            #dep -= 1
            arr[r][c] = 0

dfs(pos[0][0], pos[0][1], 0)
