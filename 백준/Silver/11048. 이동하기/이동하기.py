n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
dp = [[0]*m for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(n):
    for j in range(m):
        if (i, j) == (n-1, m-1):
            break
        
        if i+1 < n:
            dp[i+1][j] = max(dp[i][j] + arr[i+1][j], dp[i+1][j])
        if j+1 < m:
            dp[i][j+1] = max(dp[i][j] + arr[i][j+1], dp[i][j+1])
        if i+1 < n and j+1 < m:
            dp[i+1][j+1] = max(dp[i][j] + arr[i+1][j+1], dp[i+1][j+1])

print(dp[n-1][m-1])