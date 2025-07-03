import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [0] * (n + 1)

if n == 1:
    dp[0] = lst[0]
    print(dp[0])
elif n == 2:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    print(dp[1])
else:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[0] + lst[2], lst[1] + lst[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + lst[i], dp[i - 3] + lst[i - 1] + lst[i])

    print(dp[n - 1])
