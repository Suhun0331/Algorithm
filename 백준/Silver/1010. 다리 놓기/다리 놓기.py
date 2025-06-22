import sys
input = sys.stdin.readline

MAX = 31

dp = [[0] * MAX for _ in range(MAX)]

for n in range(MAX):
    dp[n][0] = 1
    dp[n][n] = 1

for n in range(1, MAX):
    for r in range(1, n):
        dp[n][r] = dp[n-1][r-1] + dp[n-1][r]

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    print(dp[m][n])  # m C n