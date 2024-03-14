import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    stack = []
    a = list(input())
    check = 0
    for i in a:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                del stack[-1]
            else:
                check = 1
                break
    if stack or check == 1:
        print('NO')
    else:
        print('YES')
