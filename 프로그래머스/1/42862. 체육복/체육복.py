def solution(n, lost, reserve):
    answer = 0
    
    arr = [1]*(31)
    
    for i in lost:
        arr[i] -=1
    for i in reserve:
        arr[i] += 1
        
    reserve.sort()
    
    for i in reserve:
        if i not in lost:
            if arr[i-1] == 0:
                arr[i-1] += 1
                arr[i] -= 1
            elif arr[i+1] == 0:
                arr[i+1] += 1
                arr[i] -= 1
    
    for i in range(1, n+1):
        if arr[i] >= 1:
            answer += 1
            
    return answer