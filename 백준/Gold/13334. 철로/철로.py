import sys
import heapq

input = sys.stdin.readline

num = int(input())
heap = []
heap2 = []
for i in range(num):
    a, b = map(int, input().split())
    if a>b:
        a, b = b, a
    heapq.heappush(heap, (b, a))

heap = sorted(heap)
length = int(input())
max_cnt = 0
for i in heap:
    end, start = i
    heapq.heappush(heap2, start)
    start_point = end - length
    while heap2 and heap2[0] < start_point: # heap[0] = 힙에 저장된 시작 지점 중 최소값
        heapq.heappop(heap2)
    max_cnt = max(max_cnt, len(heap2))
    
print(max_cnt)
        
