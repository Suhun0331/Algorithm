def solution(N, number):
    if N == number:
        return 1
    dp = [set([int(str(N)*i)]) for i in range(1, 9)]
    
    for i in range(1, 8):
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i-j-1]:
                    dp[i].add(num1+num2)
                    dp[i].add(num1-num2)
                    dp[i].add(num1*num2)
                    if num2 != 0:
                        dp[i].add(num1//num2)
        if number in dp[i]:
            return i+1
    return -1
            
        
        
    
