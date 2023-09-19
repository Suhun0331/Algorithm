import sys

num = int(input())

lst = []
for i in range(num):
    a = list(map(str, sys.stdin.readline().split()))
    if a[0] == 'push':
        lst.insert(0,int(a[1]))
    elif a[0] == 'front':
        if not lst:
            print(-1)
        else:
            print(lst[len(lst)-1])
    elif a[0] == 'back':
        if not lst:
            print(-1)
        else:
            print(lst[0])
    elif a[0] == 'size':
        print(len(lst))
    elif a[0] == 'empty':
        if not lst:
            print(1)
        else:
            print(0)
    elif a[0] == 'pop':
        if not lst:
            print(-1)
        else:
            print(lst.pop())