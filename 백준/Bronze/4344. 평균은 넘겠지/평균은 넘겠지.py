num = int(input())
lst = []
for i in range(num):
    sum = 0
    cnt = 0
    lst = list(map(int, input().split()))
    for i in range(1, len(lst)):
        sum += lst[i]
    avg = sum/(len(lst)-1)
    for i in range(1, len(lst)):
        if lst[i]>avg:
            cnt += 1
    print("%.3f%%"%(cnt/(len(lst)-1)*100))
    
