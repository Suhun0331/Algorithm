a = int(input())
lst = list(map(int, input().split()))
summ = a
for i in range(a):
    for j in range(2, lst[i]):
        if(lst[i] % j == 0):
            summ -= 1
            break
if 1 in lst:
    summ -= 1
print(summ)