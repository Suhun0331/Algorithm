n, m = map(int, input().split())
arr = list(map(int ,input().split()))
arr.sort()
lst = []
visited = [False] * (n+1)
dup = set()
def dfs(startIdx):
    #print(dup)
    if len(lst) == m:
        dup.add(tuple(lst))
        #print(' '.join(map(str, lst)))
        return
    
    for i in range(n):
        if not visited[i]:
            lst.append(arr[i])
            visited[i] = True
            dfs(i)
            lst.pop()
            visited[i] = False
            
dfs(0)
dup = list(dup)
dup.sort()
for i in dup:
    for j in i:
        print(j, end = ' ')
    print()
