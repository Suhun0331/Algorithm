import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.pop()

def move(start, end):
  if start == end:
    return 1
  if start == 0:
    return 2
  if abs(start-end) == 2:
    return 4
  else:
    return 3

dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(len(arr)+1)]

dp[0][0][0] = 0

for i in range(len(arr)):
  target = arr[i]
  for r in range(5):
    for l in range(5):
      # 다음 스텝 왼발
      dp[i+1][target][l] = min(dp[i+1][target][l], dp[i][r][l]+move(r, target))
      # 다음 스텝 오른발
      dp[i+1][r][target] = min(dp[i+1][r][target], dp[i][r][l]+move(l, target))


answer = float('inf')
# print(dp[len(arr)-1])
for i in range(5):
  answer = min(answer, dp[len(arr)][arr[-1]][i])
  answer = min(answer, dp[len(arr)][i][arr[-1]])

print(answer)