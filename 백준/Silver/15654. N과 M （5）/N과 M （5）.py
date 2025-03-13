n, m = map(int, input().split())
arr = list(map(int ,input().split()))
arr.sort()
lst = []
visited = [False] * (n+1)
def dfs(startIdx):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(n):
        if not visited[i]:
            lst.append(arr[i])
            visited[i] = True
            dfs(i)
            lst.pop()
            visited[i] = False
            
dfs(0)

