import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x : x[1])
heap = []
for i in arr:
    heapq.heappush(heap, i[0])
    if len(heap) > i[1]:
        heapq.heappop(heap)
print(sum(heap))
    
