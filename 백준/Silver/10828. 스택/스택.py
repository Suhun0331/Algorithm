import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    ans = list(sys.stdin.readline().split())
    if ans[0] == 'push':
        num = int(ans[1])
        stack.append(num)

    elif ans[0] == 'pop':
        if stack:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
    elif ans[0] == 'size':
        print(len(stack))
    elif ans[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif ans[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
