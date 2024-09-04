import heapq

n = list(map(int, input()))
heap = []

for i in n:
    heapq.heappush(heap, -i)

#print(n)
#print(sum(n))
num = ''
if sum(n)%3 != 0 or 0 not in n:
    print(-1)
else:
    while heap:
        print(-heapq.heappop(heap), end = '')


