'''
우선순위 큐

대기큐 = 우선순위 큐이고, 걸리는 시간 / 들어온 시간 / 번호 순 우선순위 ?
아니면 그냥 큐 구현해서 작업 들어올 때마다 sort ?

1. jobs 500, 하나당 1 ~ 1000 -> 최대 시간 500000 이라서 전체 for문 돌아도 될 거 같은데
일단 이렇게 풀고, 그 이후에 최적화 하는 방법을 찾아보자

우선순위 큐는 앞에서부터 우선순위 매김 -> [걸리는 시간 / 들어온 시간 / 인덱스] 형태 저장?
----------------
너무 막막해서 풀이 참고함

now로 현재 시간 저장
jobs를 돌면서 jobs[0]이 현재 시간보다 전에 있으면 힙에 넣어줌
그렇게 다 넣은 후, 힙에서 가장 먼저 나오는 우선순위의 작업을 뽑고
걸리는 시간만큼 now에 더해줌.
만약 힙에 아무것도 없으면 레디큐에 아무것도 없다는 뜻이니까 now += 1
'''
import heapq as hq

def solution(jobs):
    heap = []
    now = 0
    finish = 0
    answer = 0
    check = -1

    while finish < len(jobs):
        for job in jobs:
            if now >= job[0] > check:
                hq.heappush(heap, (job[1], job[0]))
        
        if heap:
            time, start = hq.heappop(heap)
            check = now
            now += time
            answer += (now - start)
            finish += 1
        else:
            now += 1
    return answer // len(jobs)
    
        
            
            
    
    




