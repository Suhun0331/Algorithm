n = int(input())

miro = list(map(int,input().split()))
miro.insert(0, 0)

dp = [1001]*(n+1)
dp[1] = 0

for i in range(1, n+1):
    for j in range(1,miro[i]+1):
        if i+j <= n:
            dp[i+j] = min(dp[i+j], dp[i]+1)
        else:
            break


if dp[n] == 1001:
    print(-1)
else:
    print(dp[n])