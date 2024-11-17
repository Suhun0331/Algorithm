n = int(input())
connect = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(connect):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(i):
    global ans
    visited[i] = 1
    ans += 1

    for n in arr[i]:
        if visited[n] == 0:
            dfs(n)


visited = [0] * (n+1)
ans = 0
dfs(1)
print(ans-1)

