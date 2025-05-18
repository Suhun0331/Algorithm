import sys

input = sys.stdin.readline

sent = input().strip()
stack = []
for i in sent:
    if i == "(":
        stack.append(i)
    elif i == ")":
        temp = 0
        while True:
            ans = stack.pop()
            if ans == "(":
                break
            temp += ans
        stack.append(temp)
    elif i == 'H':
        stack.append(1)
    elif i == 'C':
        stack.append(12)
    elif i == 'O':
        stack.append(16)
    else:
        stack.append(stack.pop() * int(i))

print(sum(stack))