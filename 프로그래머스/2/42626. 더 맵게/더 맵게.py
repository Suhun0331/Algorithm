import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)
        heapq.heappush(scoville, num1+num2*2)
        answer += 1
    return answer