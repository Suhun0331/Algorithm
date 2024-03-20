import sys
import heapq
input = sys.stdin.readline
num = int(input())
heap = []
for _ in range(num):
    n = int(input())
    n *= -1
    if n == 0:
        if heap:
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,n)
