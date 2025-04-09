'''
이건 gpt의 풀이
유일하게 힙 구조 유지하면서 값 변경, visited 관리를 통해 시간도 효율적.
'''
import heapq as hq
def solution(operations):
    minheap = []
    maxheap = []
    visited = [False] * len(operations)
    
    for i, oper in enumerate(operations):
        if oper == 'D 1':
            while maxheap and not visited[maxheap[0][1]]:
                hq.heappop(maxheap)
            if maxheap:
                visited[maxheap[0][1]] = False
                hq.heappop(maxheap)
        elif oper == 'D -1':
            while minheap and not visited[minheap[0][1]]:
                hq.heappop(minheap)
            if minheap:
                visited[minheap[0][1]] = False
                hq.heappop(minheap)
        else:
            hq.heappush(minheap, (int(oper[2:]) ,i))
            hq.heappush(maxheap, (int(oper[2:]) * (-1) ,i))
            visited[i] = True
                
    while minheap and not visited[minheap[0][1]]:
            hq.heappop(minheap)
    while maxheap and not visited[maxheap[0][1]]:
            hq.heappop(maxheap)
            
    if not minheap:
        return [0,0]
    else:
        return [-maxheap[0][0], minheap[0][0]]
    
    
    
    
    
    
    