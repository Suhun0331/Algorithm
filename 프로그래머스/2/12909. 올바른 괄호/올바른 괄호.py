def solution(s):
    answer = True
    stack = []
    for i in s:
        if not stack and i == ')':
            return False
        elif i == '(':
            stack.append(i)
        else:
            stack.pop()
    return False if stack else True
