'''
찾아본 방법으로 내가 다시 작성한 코드 
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
for i in range(3):
    dp = [[1001]*3 for _ in range(n)]
    dp[0][i] = arr[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + arr[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + arr[j][1]
        dp[j][2] = min(dp[j-1][1], dp[j-1][0]) + arr[j][2]
    dp[-1][i] = float('inf')
    answer = min(answer, min(dp[-1]))
print(answer)