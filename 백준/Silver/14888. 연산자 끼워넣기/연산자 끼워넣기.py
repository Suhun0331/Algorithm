'''
dfs라고 생각하면 될 듯.
매 순간에 + - * /일 때를 모두 생각해서 재귀 호출
재귀 호출과 동시에 해당 연산자 값 -1
깊이가 끝에 도달했을 때 기존 max,min 값과 새 값 비교해서 넣어주기
'''

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
oper = list(map(int, input().split()))

maxx = -1000000000
minn = 1000000000
total = arr[0]

def dfs(dep, add, minus, mul, div, total):
    global maxx, minn
    #print(total)
        
    if dep == n:
        maxx = max(total, maxx)
        minn = min(total, minn)
        return
    
    if add:
        oper[0] -= 1
        dfs(dep+1, oper[0], oper[1], oper[2], oper[3],total+arr[dep])
        oper[0] += 1
    if minus:
        oper[1] -= 1
        dfs(dep+1, oper[0], oper[1], oper[2], oper[3], total-arr[dep])
        oper[1] += 1
    if mul:
        oper[2] -= 1
        dfs(dep+1, oper[0], oper[1], oper[2], oper[3], total*arr[dep])
        oper[2] += 1
    if div:
        oper[3] -= 1
        if total < 0:
            dfs(dep+1, oper[0], oper[1], oper[2], oper[3], (-1)*((total*(-1))//arr[dep]))
        else:
            dfs(dep+1, oper[0], oper[1], oper[2], oper[3], total//arr[dep])
        oper[3] += 1

dfs(1, oper[0], oper[1], oper[2], oper[3], total)
print(maxx)
print(minn)
