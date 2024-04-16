import sys
import heapq

input = sys.stdin.readline

num = int(input())

lst = []
for i in range(num):
    a, b = map(int, input().split())
    lst.append((a, b))
lst = sorted(lst)
heap = []
max_cnt = 0
for i in lst:
    start, end = i
    heapq.heappush(heap, end)
    if heap[0] <= start:
        heapq.heappop(heap)
    max_cnt = max(max_cnt, len(heap))
print(max_cnt)
