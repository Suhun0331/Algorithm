n, m = map(int, input().split())

visited = [False] * (n+1)
s = []
check = []
def dfs(start):
    if len(s) == m:
        '''
        sort_s = sorted(s)
        for j in check:
            if sort_s == j:
                return
        check.append(s[:])
        '''
        
        for i in s:
            print(i, end = ' ')
        print()
        return
    for i in range(start, n+1):
        if visited[i]:
            continue
        s.append(i)
        visited[i] = True
        dfs(i)
        s.pop()
        visited[i] = False

dfs(1)
