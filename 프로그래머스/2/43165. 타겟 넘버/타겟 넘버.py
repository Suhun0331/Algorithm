count = 0

def dfs(step, sum, numbers, target):
    global count

    if sum == target and step == len(numbers):
        count += 1
        return
    if step >= len(numbers):
        return
    #print(sum)
    
    dfs(step + 1, sum + numbers[step], numbers, target)
    dfs(step + 1, sum - numbers[step], numbers, target)
    
        

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    
    return count