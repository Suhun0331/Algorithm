lst = list(input())

answer = [] # 정답 저장 리스트
stack = [] # 연산자 저장 리스트

for i in range(len(lst)):
    if lst[i].isalpha():
        answer.append(lst[i])
    elif lst[i] == '(':
        stack.append(lst[i])
    elif lst[i] == ')':
        while stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    else:
        if lst[i] == '+' or lst[i] == '-':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())
            stack.append(lst[i])
        elif lst[i] == '*' or lst[i] == '/':
            if stack and (stack[-1] == '*' or stack[-1]=='/'):
                answer.append(stack.pop())
                stack.append(lst[i])
            else:
                stack.append(lst[i])
while stack: # stack에 남은 연산자 마저 처리
    answer.append(stack.pop())
for i in answer:
    print(i, end = '')