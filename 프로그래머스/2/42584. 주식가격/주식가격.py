'''
스택 / 큐 중 어떤거?

스택 사용.
price로 들어온 값 스택에 저장하는데, 맨 위에 있는 값이 들어온 값보다 크면 맨 위 pop
스택에 값 저장할 때 가격, 인덱스 같이 저장하고
pop 하게되면 answer[인덱스] += (새 인덱스-pop한값 인덱스)
'''
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, val in enumerate(prices): # 1 5 6 3
        #print(stack)
        if i == 0 or not stack:
            stack.append((val, i))
            continue
            
        if val >= stack[-1][0]:
            stack.append((val, i))
        else:
            while val < stack[-1][0] :
                _, ind = stack.pop()
                answer[ind] += (i - ind)
                if not stack:
                    break
            stack.append((val, i))
            
    for i in stack:
        value, index = i
        answer[index] += len(prices) - index - 1
    return answer
    
    
    
    
    