import sys
import heapq

input = sys.stdin.readline

num = int(input())
max_heap = []
min_heap = []

for _ in range(num):
    n = int(input())
    if n == 0:
        if max_heap and min_heap:
            if abs(max_heap[0]) < abs(min_heap[0]):
                print(heapq.heappop(max_heap))
            else:
                print(heapq.heappop(min_heap)*(-1))
        elif max_heap:
            print(heapq.heappop(max_heap))
        elif min_heap:
            print(heapq.heappop(min_heap)*(-1))
        else:
            print(0)
    else:
        if n > 0:
            heapq.heappush(max_heap,n)
        else:
            heapq.heappush(min_heap,-n)
