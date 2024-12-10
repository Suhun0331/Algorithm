n, k = map(int, input().split())

arr = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(k+1):
        if j-w >= 0:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-w] + v)
        else:
            arr[i][j] = arr[i-1][j]
print(arr[n][k])
