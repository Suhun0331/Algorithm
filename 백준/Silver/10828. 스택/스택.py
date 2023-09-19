import sys

num = int(input())

lst = []

for _ in range(num):
    a = list(map(str, sys.stdin.readline().split()))
    if len(a) == 1:
        ans = a[0]
    elif len(a) == 2:
        ans = a[0]
        ans2 = a[1]
        
    if ans == 'push':
        lst.append(int(ans2))
        
    if ans == 'pop' and len(lst) != 0:
        number = lst[len(lst)-1]
        del lst[len(lst)-1]
        print(number)
    elif ans == 'pop':
        print(-1)
        
        
    if ans == 'top' and len(lst) != 0:
        print(lst[len(lst)-1])
    elif ans == 'top':
        print(-1)

    if ans == 'empty'and len(lst) == 0:
        print(1)
    elif ans == 'empty'and len(lst) != 0:
        print(0)

    if ans == 'size':
        print(len(lst))