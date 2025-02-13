import sys
from collections import deque

def process_keystrokes(log):
    left_stack = deque()
    right_stack = deque()
    
    for char in log:
        if char == '-':  # 백스페이스 (왼쪽 삭제)
            if left_stack:
                left_stack.pop()
        elif char == '<':  # 커서 왼쪽 이동
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif char == '>':  # 커서 오른쪽 이동
            if right_stack:
                left_stack.append(right_stack.popleft())
        else:
            left_stack.append(char)  # 일반 문자 입력

    return ''.join(left_stack) + ''.join(right_stack)  # 최종 문자열 반환

# 입력 처리
t = int(sys.stdin.readline().strip())  # 테스트 케이스 개수
for _ in range(t):
    log = sys.stdin.readline().strip()
    print(process_keystrokes(log))
