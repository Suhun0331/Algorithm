n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

visited = [[0]*m for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
def bfs(si, sj, ei, ej):

    q = []
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.pop(0)
        if ci == ei and cj == ej:
            return visited[ci][cj]

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<= ni< n and 0<= nj < m and not visited[ni][nj] and arr[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1


ans = bfs(0, 0, n-1, m-1)
print(ans)