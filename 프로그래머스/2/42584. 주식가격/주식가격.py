'''
스택 / 큐 중 어떤거?

스택 사용.
price로 들어온 값 스택에 저장하는데, 맨 위에 있는 값이 들어온 값보다 크면 맨 위 pop
스택에 값 저장할 때 가격, 인덱스 같이 저장하고
pop 하게되면 answer[인덱스] += (새 인덱스-pop한값 인덱스)

+ 약간의 코드 최적화 + 더 최적화  
'''
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, val in enumerate(prices):
        while stack and val < stack[-1][0] :
            _, ind = stack.pop()
            answer[ind] += (i - ind)
        stack.append((val, i))
            
    for i in stack:
        value, index = i
        answer[index] += len(prices) - index - 1
        
    return answer