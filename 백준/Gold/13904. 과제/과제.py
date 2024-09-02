import sys
import heapq

input = sys.stdin.readline

n= int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
heap = []
for i in arr:
    heapq.heappush(heap, i[1])
    if len(heap) > i[0]:
        heapq.heappop(heap)
print(sum(heap))
