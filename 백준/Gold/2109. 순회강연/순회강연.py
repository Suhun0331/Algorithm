'''
아니 이 아이디어를 어떻게 생각해 도대체 ..?
d 기준, p 기준으로 정렬해서 처리했는데 틀렸길래
반례 찾아봤더니 아예 푸는 방법이 틀린걸 알게됨
최소 힙 사용하는 문제였고, 이해는 됐는데
이걸 대체 어떻게 스스로 생각해야 할지 모르겠음. 
'''
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
    
