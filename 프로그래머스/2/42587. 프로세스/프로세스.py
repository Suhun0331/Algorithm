from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    target = location
    while q:
        print(q, target)
        if q[0] == max(q):
            if target == 0:
                answer += 1
                return answer
            q.popleft()
            answer += 1
            target -= 1
            continue
        q.append(q.popleft())
        if target == 0:
            target = len(q)-1
        else:
            target -= 1
    
    return answer


