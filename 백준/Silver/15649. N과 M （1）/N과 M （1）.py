n, m = map(int, input().split())

visited = [False] * (n+1)
s = []
def dfs():
    if len(s) == m:
        for i in s:
            print(i, end = ' ')
        print()
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False

dfs()
