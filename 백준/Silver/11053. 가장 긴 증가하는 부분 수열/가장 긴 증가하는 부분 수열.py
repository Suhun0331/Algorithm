import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr.insert(0,0)

dp = [0] * (n+1)
dp[1] = 1

'''
for i in range(2, n+1):
    for j in range(1, i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
'''


for i in range(2, n+1):
    for j in range(1, i):
        if arr[i] > arr[j] and dp[i] <= dp[j]:
            dp[i] = dp[j]+1
    if dp[i] == 0:
        dp[i] += 1

    
print(max(dp))
            
