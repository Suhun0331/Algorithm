import sys

a = list(sys.stdin.readline())
answer = 0
lazer = 0
stick = 0
stack= []
possible = False

for i in a:
    if i == '(':
        stack.append(i)
        possible = True
        
    elif i == ')':
        if possible == True:
            possible = False
            lazer += 1
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()

stick = int((len(a) - lazer*2)/2)
answer += stick
print(answer)