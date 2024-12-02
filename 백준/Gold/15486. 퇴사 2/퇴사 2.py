import sys
input= sys.stdin.readline

n = int(input())
arr = []
dp = [0]*(n+1)
dp[0] = 0

for i in range(n):
    a, b = map(int,input().split())
    dp[i] = max(dp[i], dp[i-1])
    if i+a <= n :
        dp[i+a-1] = max(dp[i+a-1], dp[i-1] + b)

        
print(dp[n-1])
