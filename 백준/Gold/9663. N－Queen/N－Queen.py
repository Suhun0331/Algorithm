n = int(input())

lst = [0]*n
ans = 0
def promising(x):
    for i in range(x):
        if lst[i]==lst[x] or abs(lst[i]-lst[x])==abs(i-x):
            return False
    return True

def dfs(x):
    global ans
    if n == x:
        ans += 1
        return
    else:
        for i in range(n):
            lst[x] = i
            if promising(x):
                dfs(x+1)
dfs(0)
print(ans)
        
