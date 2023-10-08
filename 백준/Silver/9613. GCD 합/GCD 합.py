import math


num = int(input())

for i in range(num):
    lst = list(map(int,input().split()))
    summ = 0
    for j in range(1, len(lst)-1):
        for k in range(j+1, len(lst)):
            summ += (math.gcd(lst[j],lst[k]))
    print(summ)


''' 유클리드 호제법 풀
def gcd(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b

num = int(input())

for i in range(num):
    lst = list(map(int,input().split()))
    summ = 0
    for j in range(1, len(lst)-1):
        for k in range(j+1, len(lst)):
            summ += (gcd(lst[j],lst[k]))
    print(summ)
'''
