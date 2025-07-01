'''
stack 사용

스택에 값 하나씩 넣다가 목표 단어의 끝글자랑 같으면 스택 앞에꺼 검사
중간에 다른거 있으면 다시 값 넣기

값 지우는걸 어떡하지?
다 맞으면 목표 길이만큼 슬라이싱으로 지우기?

'''

stack = []
sentence = list(input())
target = list(input())

for i in range(len(sentence)):
    #print(''.join(stack))
    if sentence[i] != target[-1]:
        stack.append(sentence[i])
        continue
    else:
        stack.append(sentence[i])
        if target == stack[-len(target):]:
            del stack[-len(target):]
            
if stack:
    print(''.join(stack))
else:
    print('FRULA')
