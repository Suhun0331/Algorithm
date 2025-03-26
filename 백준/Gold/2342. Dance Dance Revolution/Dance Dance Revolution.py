'''
시간 1/3짜리 코드
dp를 3차원배열 만드는게 아니라 2차원배열 하나 만들어서 계속 업데이트 시켜주는 방식
'''
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

dp = [[float('inf')] * 5 for _ in range(5)]

dp[0][0] = 0

for i in range(len(arr)):
  target = arr[i]
  new_dp = [[float('inf')]*5 for _ in range(5)]
  for r in range(5):
    for l in range(5):
      current = dp[l][r]
      # 다음 스텝 왼발
      if target != r:
        new_dp[target][r] = min(new_dp[target][r], current + move(l, target))

      # 다음 스텝 오른발
      if target != l:
        new_dp[l][target] = min(new_dp[l][target], current + move(r, target))
  dp = new_dp

answer = float('inf')
for i in range(5):
  for j in range(5):
    answer = min(dp[i][j], answer)
print(answer)