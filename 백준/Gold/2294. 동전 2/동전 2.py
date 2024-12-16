n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0
for i in coin:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i] + 1)
    #print(dp)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
