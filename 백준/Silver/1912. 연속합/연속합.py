import sys
n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = lst[0]
    else:
        dp[i] = lst[i]
        if dp[i] < dp[i-1] + lst[i]:
            dp[i] = dp[i-1] + lst[i]
print(max(dp))