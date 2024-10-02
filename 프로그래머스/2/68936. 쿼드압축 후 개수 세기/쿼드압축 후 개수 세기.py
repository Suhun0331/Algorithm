one = 0
zero = 0

def recursion(x, y, arr, n):
    global one
    global zero
    if n == 1:
        if arr[x][y] == 1:
            one += 1
            return
        else:
            zero += 1
            return
            
    check = arr[x][y]
    for i in range(n):
        for j in range(n):
            if check == arr[x + i][y + j]:
                continue
            
            recursion(x, y, arr, n//2)
            recursion(x + n//2, y, arr, n//2)
            recursion(x, y + n//2, arr, n//2)
            recursion(x+ n//2 , y + n//2, arr, n//2)
            return
        
    if check == 1:
        one += 1
    else:
        zero += 1
    

def solution(arr):
    recursion(0, 0, arr, len(arr))
    answer = []
    answer.append(zero)
    answer.append(one)
    return answer