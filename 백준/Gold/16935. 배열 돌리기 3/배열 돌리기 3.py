'''

'''
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split()) #n : 세로길이, m : 가로길이

arr = [list(map(int, input().split())) for _ in range(n)]


def one(arr):
    answer = []
    for i in range(n):
        answer.append(arr[n-i-1])
    return answer

def two(arr):
    answer = []
    for i in arr:
        i.reverse()
        answer.append(i)
    return answer

def three(arr):
    global n, m
    answer = []
    sub = []
    for i in range(m):
        for j in range(n):
            sub.append(arr[n-j-1][i])
        answer.append(sub)
        sub = []
    n , m = m, n
    return answer

def four(arr):
    global n, m
    answer = []
    sub = []
    for i in range(m-1, -1, -1):
        for j in range(n):
            sub.append(arr[j][i])
        answer.append(sub)
        sub = []
    n , m = m, n
    return answer

def five(arr): #n : 세로길이, m : 가로길이
    answer = []
    sub = []
    for i in range(n//2): #0 ~ 2
        sub = []
        sub1 = []
        sub2 = []
        sub1 = (arr[n//2+i][0:(m//2)])
        sub2 = (arr[i][0:(m//2)])
        sub1.extend(sub2)
        answer.append(sub1)
    
    for i in range(n//2):
        sub = []
        sub1 = []
        sub2 = []
        sub1 = (arr[n//2+i][m//2:m])
        sub2 = (arr[i][m//2:m])
        
        sub1.extend(sub2)
        answer.append(sub1)
        
    return answer

def six(arr): #n : 세로길이, m : 가로길이
    answer = []
    sub = []
    for i in range(n//2): #0 ~ 2
        sub = []
        sub1 = []
        sub2 = []
        sub1 = (arr[i][m//2:m])#(arr[n//2+i][0:(m//2)])
        sub2 = (arr[n//2+i][m//2:m])#(arr[i][0:(m//2)])
        sub1.extend(sub2)
        answer.append(sub1)
    
    for i in range(n//2):
        sub = []
        sub1 = []
        sub2 = []
        sub1 = (arr[i][0:(m//2)])#(arr[n//2+i][m//2:m])
        sub2 = (arr[n//2+i][0:(m//2)])#(arr[i][m//2:m])
        
        sub1.extend(sub2)
        answer.append(sub1)
        
    return answer


order = list(map(int, input().split()))

for i in order:
    if i == 1:
        arr = one(arr)
        
    elif i == 2:
        arr = two(arr)
        
    elif i == 3:
        arr = three(arr)
        
    elif i == 4:
        arr = four(arr)
        
    elif i == 5:
        arr = five(arr)
        
    elif i == 6:
        arr = six(arr)
        

for i in arr:
    for j in i:
        print(j, end = ' ')
    print()
