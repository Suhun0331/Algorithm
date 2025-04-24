'''
1차 제출 -> 시간초과
reverse 계속 하면 시간 너무 오래걸림 -> R이 몇 번 나왔는지에 따라서 pop할지 popleft할지 결정
reverse를 안한단 뜻.
마지막 출력할 때에도 그거에 맞게 앞에서부터 / 뒤에서부터
-> 또 실패
반례 못찾겠어서 질문게시판 봄 -> 빈 리스트일 때 R이면 에러 안나야하는데
초반 예외처리로 설정 해버려서 반례가 생김 -> 초반 예외에 조건 추가
'''
import sys
from collections import deque
t = int(input())

for i in range(t):
    error = False
    order = input()
    num = int(input())
    lst = input()
    R = True # true -> 왼쪽부터, false -> 오른쪽부터 
    if len(lst) == 2 and 'D' in order:
        print('error')
        continue
    q = deque((lst[1:-1].split(',')))
    # print(q)
    for i in order:
        if i == 'R':
            if R:
                R = False
            else:
                R = True
        elif i == 'D':
            if not q:
                print('error', end = '')
                error = True
                break
            if R:
                q.popleft()
            else:
                q.pop()
    q = list(q)
    if len(q) > 2:
        for i in range(len(q)):
            q[i] = int(q[i])
    if not error:
        print('[', end = '')
        if R:
            for i in range(len(q)):
                if i != (len(q) - 1):
                    print(q[i], end = ',')
                else:
                    print(q[i], end = '')
        else:
            for i in range(len(q)-1, -1, -1):
                if i != 0:
                    print(q[i], end = ',')
                else:
                    print(q[i], end = '')
        print(']', end = '')
    print()
        # print(list(q))
        
    
