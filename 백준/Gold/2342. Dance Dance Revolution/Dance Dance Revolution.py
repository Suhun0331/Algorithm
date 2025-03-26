'''
인터넷 풀이, 이해 하는데도 한참 걸림
'''
import sys
input = sys.stdin.readline
INF = float('inf')

# 이동할 때 드는 비용 계산
def move_cost(from_pos, to_pos):
    if from_pos == 0:
        return 2
    elif from_pos == to_pos:
        return 1
    elif abs(from_pos - to_pos) == 2:
        return 4
    else:
        return 3

# 입력
steps = list(map(int, input().split()))
steps.pop()  # 0은 입력의 끝

# DP 초기화: dp[step][left][right] = 최소 힘
dp = [[[INF] * 5 for _ in range(5)] for _ in range(len(steps)+1)]
dp[0][0][0] = 0  # 시작 위치: 양 발이 중앙(0)에 있을 때

# DP 수행
for i in range(len(steps)):
    target = steps[i]
    for l in range(5):
        for r in range(5):
            # 왼발을 target으로 이동
            dp[i+1][target][r] = min(dp[i+1][target][r], dp[i][l][r] + move_cost(l, target))
            # 오른발을 target으로 이동
            dp[i+1][l][target] = min(dp[i+1][l][target], dp[i][l][r] + move_cost(r, target))

# 결과: 마지막 step의 모든 left, right 조합 중 최소값
result = INF
for l in range(5):
    for r in range(5):
        result = min(result, dp[len(steps)][l][r])

print(result)
