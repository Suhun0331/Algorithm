def solution(money):
    answer = 0
    first = False
    dp = [0] * len(money)
    
    # 첫 번째 집을 선택하는 경우 (마지막 집은 선택할 수 없음)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money) - 1):  # 마지막 집 제외
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    max1 = dp[len(money) - 2]  # 마지막 집을 제외한 경우의 최대값 저장
    
    # 첫 번째 집을 선택하지 않는 경우 (마지막 집 선택 가능)
    dp[0] = 0  # 첫 번째 집 선택 X
    dp[1] = money[1]
    for i in range(2, len(money)):  # 마지막 집 포함 가능
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    max2 = dp[len(money) - 1]  # 마지막 집까지 포함한 경우의 최대값 저장
    
    return max(max1, max2)
