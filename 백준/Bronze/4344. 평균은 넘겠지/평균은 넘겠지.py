num = int(input())
lst = []
for i in range(num):
    cnt = 0
    lst = list(map(int, input().split()))
    avg = sum(lst[1:])/lst[0]
    for i in lst[1:]:
        if i>avg:
            cnt += 1
    print("%.3f%%"%(cnt/lst[0]*100))
    
