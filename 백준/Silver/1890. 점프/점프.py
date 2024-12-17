n = int(input())

jump = []

for i in range(n):
    jump.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0 and jump[i][j] != 0:
            if i + jump[i][j] < n:
                dp[i+jump[i][j]][j] += dp[i][j]
            if j + jump[i][j] < n:
                dp[i][j+jump[i][j]] += dp[i][j]
            
print(dp[n-1][n-1])