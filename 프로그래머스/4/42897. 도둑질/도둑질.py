def solution(money):
    answer = 0
    dp1 = []
    dp2 = []
    
    # 첫 번째 집 사용
    dp1.append(money[0])
    dp1.append(dp1[0])
    
    dp2.append(0)
    dp2.append(money[1])
    
    for i in range(2, len(money)):
        if i != len(money) -1:
            dp1.append(max(dp1[i-1], dp1[i-2] + money[i]))
        dp2.append(max(dp2[i-1], dp2[i-2] + money[i]))
        
    return max(dp1[-1], dp2[-1])
