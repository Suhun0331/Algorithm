'''
각자 걸리는 날짜 리스트 만들기
앞에서부터 기준이 돼서 popleft 하면서 확인
다음 숫자가 pop 한 숫자보다 작으면 count += 1하고 같이 pop
리스트 빌 때까지 반복
'''
from collections import deque
def solution(progresses, speeds):
    answer = deque()
    
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            answer.append((100-progresses[i])//speeds[i])
        else:
            answer.append((100-progresses[i])//speeds[i] + 1)
    cnt = 1
    ans = []
    print(answer)
    pop = answer.popleft()
    while answer:
        if answer[0] <= pop:
            answer.popleft()
            cnt += 1
        
        else:
            ans.append(cnt)
            pop = answer.popleft()
            cnt = 1
        if not answer:
                ans.append(cnt)
        
    
    return ans