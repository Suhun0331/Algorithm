n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

visited = [[0]*m for _ in range(n)]


def bfs(si, sj, ei, ej):
    q = []
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (ei , ej):
            return arr[ei][ej]
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                arr[ni][nj] = arr[ci][cj] + 1

print(bfs(0, 0, n-1, m-1))