import sys
import heapq

input = sys.stdin.readline

num = int(input())
heap = []

for _ in range(num):
    n = int(input())
    if n == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(n),n))
