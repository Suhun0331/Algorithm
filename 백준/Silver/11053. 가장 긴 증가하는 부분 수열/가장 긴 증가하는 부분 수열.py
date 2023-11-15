n = int(input())

a = list(map(int,input().split()))
a.insert(0,0)
dp = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i):
        if i == 1:
            dp[1] = 1
            break
        else:
            if a[i] > a[j] and dp[i]<dp[j]:
                dp[i] = dp[j]
    dp[i] += 1
print(max(dp))