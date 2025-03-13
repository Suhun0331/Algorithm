n, m = map(int, input().split())
arr = list(map(int ,input().split()))
arr.sort()
lst = []
def dfs(startIdx):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(n):
        if arr[i] not in lst:
            lst.append(arr[i])
            dfs(i)
            lst.pop()
            
dfs(0)

