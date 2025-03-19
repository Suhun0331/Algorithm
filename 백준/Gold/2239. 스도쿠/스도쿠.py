'''
0인 곳의 좌표 확인, 가로확인 세로확인 네모 확인 함수 만들기
0인 곳의 좌표마다 가로세로네모 확인 후 해당 숫자가 들어갈 수 있으면
숫자 넣고 다음 좌표로 재귀
숫자 못들어가면 return하고 그 전 숫자 다음숫자로 바꾸기 반복

재귀의 깊이가 0인 곳의 좌표 개수와 같아지면 다 채운거니까 출력

가로 확인 - 몇 행인지랑 확인할 숫자 받아서 해당 행에 숫자 있는지 확인
세로 확인 - 몇 열인지랑 확인할 숫자 받아서
네모 확인 - 012 / 345/ 678 -> 행, 열 받음 / r//3*3, c//3*3 ~ 3번씩 반복
'''
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
    arr.append(list(map(int, input().strip())))

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
                print(j, end = '')
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

    
    
