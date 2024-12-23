import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = input().strip()
    stack = []
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                stack.append(0)
                break
    #print(stack)
    if stack:
        print('NO')
    else:
        print('YES')

            
