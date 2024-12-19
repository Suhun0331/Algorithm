#from collections import deque
import heapq
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):

    k = int(input())

    arr = list(map(int, input().split()))

    heapq.heapify(arr)

    #arr = deque(sorted(arr))
    answer = 0
    while len(arr) != 1:
        #print(arr, answer)
        a = heapq.heappop(arr) + heapq.heappop(arr)
        answer += a
        heapq.heappush(arr, a)
        
    print(answer)
