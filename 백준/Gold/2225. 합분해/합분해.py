n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]


for i in range(k+1):
    for j in range(n+1):
        if j == 0 and i != 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000000
        
print(dp[k][n]%1000000000)