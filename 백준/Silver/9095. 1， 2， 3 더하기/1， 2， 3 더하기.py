import sys

n = int(sys.stdin.readline())

lst = [0]*11

for k in range(1, 11):
    summ = 0
    if k == 1:
        lst[k] = 1
    elif k == 2:
        lst[k] = 2
    elif k == 3:
        lst[k] = 4
    else:
        lst[k] = lst[k-1]+lst[k-2]+lst[k-3]

for i in range(n):
    a = int(sys.stdin.readline())
    print(lst[a])