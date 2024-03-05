import sys
n, m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

start, end = 1, max(lst)

while start <= end:
    mid = (start+end)//2
    summ = 0
    
    for i in lst:
        if i > mid:
            summ += (i - mid)
    if summ < m:
        end = mid-1
    else:
        start = mid+1


print(end)
