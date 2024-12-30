import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

for i in arr2:
    start = 0
    end = len(arr)-1
    mid = (start + end) // 2
    while start <= end:
        if i > arr[mid]:
            start = mid+1
            mid = (start + end) // 2
        elif i < arr[mid]:
            end = mid - 1
            mid = (start + end) // 2
        else:
            break
    if arr[mid] != i:
        print(0)
    else:
        print(1)
        
        
            
    
