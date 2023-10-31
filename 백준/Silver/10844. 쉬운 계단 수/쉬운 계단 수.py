import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for j in range(2, n+1):
    for i in range(10):
        if i == 0:
            dp[j][i] = dp[j-1][1]
        elif i == 9:
            dp[j][i] = dp[j-1][8]
        else:
            dp[j][i] = dp[j-1][i-1] + dp[j-1][i+1]
summ = 0
for i in range(10):
    summ += dp[n][i]

print(summ%1000000000)