def solution(nums):
    answer = 0
    
    arr = []
    count = 0
    
    for i in nums:
        if i not in arr:
            arr.append(i)
    
    if len(nums)//2 <= len(arr):
        answer = len(nums)//2
    else:
        answer = len(arr)

            
    return answer