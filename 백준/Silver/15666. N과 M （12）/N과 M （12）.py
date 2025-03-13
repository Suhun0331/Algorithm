n, m = map(int, input().split())
arr = list(map(int ,input().split()))
arr.sort()
lst = []
def dfs(startIdx):
    check = 0
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(startIdx, n):
        if check != arr[i]:
            check = arr[i]
            lst.append(arr[i])
            dfs(i)
            lst.pop()
            
dfs(0)

