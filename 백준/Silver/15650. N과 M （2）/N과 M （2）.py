n, m = map(int, input().split())

visited = [False] * (n+1)
s = []
check = []
def dfs(start):
    if len(s) == m:
        
        for i in s:
            print(i, end = ' ')
        print()
        return
    for i in range(start, n+1):
        if i in s:
            continue
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)
