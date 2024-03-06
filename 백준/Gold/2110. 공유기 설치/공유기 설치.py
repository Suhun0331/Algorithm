import sys
n, c = map(int,sys.stdin.readline().split())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst = sorted(lst)

start = 1
end = lst[-1] - lst[0]
mid = (start+end)//2
count = 0
ans = 0
while(start<=end):
    mid = (start+end)//2
    
    count = 1
    i = 0
    router = 0
    check = router+1
    while(1):
        if check > len(lst)-1:
            break
        
        if lst[check] - lst[router] >= mid:
            count += 1
            router = check
        check += 1
        

    if c > count:
        end = mid-1
    elif c <= count:
        ans = mid
        start = mid+1
print(ans)

               
