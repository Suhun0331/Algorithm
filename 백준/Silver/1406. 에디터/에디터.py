import sys


stack_l = list(sys.stdin.readline())
stack_l.pop()

num = int(sys.stdin.readline())

stack_r = []

for i in range(num):
    a = list(map(str, sys.stdin.readline().split()))
    if a[0] == 'L':
        if stack_l:
            stack_r.append(stack_l.pop())
    elif a[0] == 'D':
        if stack_r:
            stack_l.append(stack_r.pop())
    elif a[0] == 'B':
        if stack_l:
            stack_l.pop()
    elif a[0] == 'P':
        stack_l.append(a[1])

stack_r.reverse()
for i in stack_r:
    stack_l.append(i)
for i in stack_l:
    print(i, end = '')