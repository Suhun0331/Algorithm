import sys
import heapq

input = sys.stdin.readline
left_heap = []
right_heap = []
cnt = 1
num = int(input())

for _ in range(num):
    n = int(input())
    if cnt%2 == 1:
        cnt += 1
        heapq.heappush(left_heap, -n)
        if cnt > 2:
            if -left_heap[0] > right_heap[0]:
                left = heapq.heappop(left_heap)
                right = heapq.heappop(right_heap)
                heapq.heappush(left_heap, -right)
                heapq.heappush(right_heap, -left)
                

        print(-left_heap[0])    
    else:
        cnt += 1
        heapq.heappush(right_heap, n)
        if -left_heap[0] > right_heap[0]:
            left = heapq.heappop(left_heap)
            right = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -right)
            heapq.heappush(right_heap, -left)

        print(-left_heap[0])
