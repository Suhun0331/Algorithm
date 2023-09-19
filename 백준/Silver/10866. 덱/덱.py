from collections import deque
import sys

num = int(sys.stdin.readline())

lst = deque()
for i in range(num):
    a = list(map(str, sys.stdin.readline().split()))

    if a[0] == 'push_front':
        lst.appendleft(a[1])
    elif a[0] == 'push_back':
        lst.append(a[1])
    elif a[0] == 'pop_front':
        if not lst:
            print(-1)
        else:
            print(lst.popleft())
    elif a[0] == 'pop_back':
        if not lst:
            print(-1)
        else:
            print(lst.pop())
    elif a[0] == 'size':
        print(len(lst))
    elif a[0] == 'empty':
        if not lst:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if not lst:
            print(-1)
        else:
            print(lst[0])
    elif a[0] == 'back':
        if not lst:
            print(-1)
        else:
            print(lst[len(lst)-1])