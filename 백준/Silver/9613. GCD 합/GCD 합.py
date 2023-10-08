import math


num = int(input())

for i in range(num):
    lst = list(map(int,input().split()))
    summ = 0
    for j in range(1, len(lst)-1):
        for k in range(j+1, len(lst)):
            summ += (math.gcd(lst[j],lst[k]))
    print(summ)
