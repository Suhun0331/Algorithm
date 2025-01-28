import sys

input = sys.stdin.readline

n = int(input())

ans = 0
lst = [0] * (n+1)

def check(x):
    for i in range(x):
        if lst[x] == lst[i] or abs(lst[x] - lst[i]) == abs(x-i):
            return False
    return True

def dfs(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            lst[x] = i
            if check(x):
                dfs(x+1)

dfs(0)
print(ans)
