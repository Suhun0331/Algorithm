def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 기존 숫자보다 큰 숫자가 나오면 제거
            k -= 1
        stack.append(num)  # 현재 숫자 추가
    
    return ''.join(stack[:len(stack) - k])  # 남은 k 처리