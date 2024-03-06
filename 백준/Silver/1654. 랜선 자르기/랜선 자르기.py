import sys

k, n = map(int,sys.stdin.readline().split())
lst = []
for i in range(k):
    lst.append(int(sys.stdin.readline()))

lst.sort()

start = 1
end = lst[-1]


while(start<=end):
    count = 0
    mid = (start+end)//2
    for i in lst:
        count += i//mid

    if count < n:
        end = mid-1
    else:
        ans = mid
        start = mid+1
print(ans)
