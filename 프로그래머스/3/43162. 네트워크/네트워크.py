from collections import deque

def solution(n, computers):
    q = deque()
    visited = [False] * n
    q.append(0)
    answer = 0
    for i in range(n):
        if visited[i]:
            continue
        q.append(i)
        while q:
            num = q.popleft()
            visited[num] = True
            for i in range(n):
                if i == num:
                    continue
                if computers[num][i] == 0:
                    continue
                if visited[i] == True:
                    continue
                q.append(i)
        answer += 1
        # 0 -> 1 3 4 5
        # 1 -> 2 5 6
        # 4 -> x
        
    
    return answer


'''
1번 컴퓨터부터 확인
1번이랑 이어진 애들 다 큐에 넣음
큐 뽑아서 그 애랑 이어진 애들 다 큐에 넣음
q 비면 answer + 1 
위 과정 싹 다 visit 처리.
1번 끝나면 2번 하는데, visit 처리 되어있으면 패스
'''
