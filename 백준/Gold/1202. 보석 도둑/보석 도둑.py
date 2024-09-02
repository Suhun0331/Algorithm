import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
bag = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(K):
    bag.append(int(input()))

# arr 리스트를 무게 기준으로 오름차순 정렬
arr.sort()
# 가방의 최대 무게를 기준으로 오름차순 정렬
bag.sort()

answer = 0
heap = []
j = 0

# 가방을 순회하며, 해당 가방에 담을 수 있는 가장 가치가 큰 물건을 선택
for i in range(K):
    while j < N and arr[j][0] <= bag[i]:
        heapq.heappush(heap, -arr[j][1])  # 최대 힙을 사용하기 위해 음수로 저장
        j += 1
    if heap:
        answer += -heapq.heappop(heap)  # 최대 힙에서 최대 가치를 가진 물건 선택

print(answer)
