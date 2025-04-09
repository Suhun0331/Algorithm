'''
트럭이 움직인다는 생각보다 그냥 순간이동 한다고 생각
트럭 2대 올라갈 수 있음 -> 다리길이 2 -> 점 2개라고 생각하기
1초에 점 1개씩 이동

큐 사용
weight 변수에는 현재 다리 위에 올라가있는 무게 저장
stack의 길이가 다리 길이보다 작거나 같을 때만 트럭 추가할 수 있음.

if 다리길이보다 다리 위 트럭 개수가 더 적은지 and 지금 추가하려는 트럭 무게 더해도 되는지:
된다면 stack에 트럭 추가
안된다면 큐의 맨 앞에 있는 트럭 통과시키기

+ 코드 최적화 
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 1
    q = deque()
    onweight = 0
    
    for wei in truck_weights:
        while True:
            if q and time > q[0][1] + bridge_length:
                onweight -= q[0][0]
                q.popleft()
            else:
                break
        while q and (onweight+wei > weight or len(q) == bridge_length):
            print(time, 'check')
            time += (bridge_length-time+q[0][1])
            onweight -= q[0][0]
            q.popleft()
        q.append((wei, time))
        time += 1
        onweight += wei
            
    if q:
        time += (bridge_length-time+q[-1][1])
                
    return time
            