'''
우선순위 큐 최댓값/최솟값 뽑아내기 ..
최대힙 / 최소힙 바꾸면 되긴 하는데 하나의 우선순위 큐에서 이걸 동시에 뽑을 수가 있나?
1. 우선순위 큐 두개 만들기(최대용/ 최소용) - 메모리 많이 듦
2. 하나만 만들고, 최댓값 뽑을 땐 다 - 붙이기 ..? - 시간 많이 듦 
'''
import heapq as hq

def solution(operations):
    minheap = []
    maxheap = []
    for i in operations:
        if i[0] == 'I':
            hq.heappush(minheap, int(i[2:]))
            hq.heappush(maxheap, int(i[2:]) * (-1))
        elif i[0] == 'D':
            if int(i[2:]) == 1 :
                if maxheap:
                    delnum = hq.heappop(maxheap)
                    delnum *= -1
                    minheap.remove(delnum)
            elif int(i[2:]) == -1:
                if maxheap:
                    delnum = hq.heappop(minheap)
                    delnum *= -1
                    maxheap.remove(delnum)
    
    if not maxheap:
        return [0,0]
    else:
        return [hq.heappop(maxheap) * (-1), hq.heappop(minheap)]
                







