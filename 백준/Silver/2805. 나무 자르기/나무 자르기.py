import sys
n, m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(lst)
ans = 0

while start <= end:
    mid = (start+end)//2
    summ = 0
    
    for i in lst:
        if i > mid:
            summ += (i - mid)
    if summ < m:
        end = mid-1
    else:
        ans = mid
        start = mid+1


print(ans)
