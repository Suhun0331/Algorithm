import sys
import heapq

input = sys.stdin.readline
left_heap = []
right_heap = []
cnt = 1
num = int(input())

for i in range(1, num+1):
    n = int(input())

    if i%2 == 1:
        heapq.heappush(left_heap, -n)
    else:
        heapq.heappush(right_heap, n)
        
    if i > 1:
        if -left_heap[0] > right_heap[0]:
            left = heapq.heappop(left_heap)
            right = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -right)
            heapq.heappush(right_heap, -left)

    print(-left_heap[0])
