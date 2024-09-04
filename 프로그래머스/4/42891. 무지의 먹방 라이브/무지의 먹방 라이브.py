import heapq

def solution(food_times, k):
    # 모든 음식이 다 먹을 수 있는 시간보다 k가 크면 종료
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐(최소 힙) 사용하여 음식을 먹는 시간을 정렬
    food_heap = []
    for i in range(len(food_times)):
        heapq.heappush(food_heap, (food_times[i], i + 1))  # (음식 시간, 음식 번호)

    total_time = 0  # 총 소비 시간
    previous_time = 0  # 이전에 제거한 음식의 시간
    food_length = len(food_times)  # 남은 음식의 개수

    # 최소 시간이 걸리는 음식부터 처리
    while total_time + (food_heap[0][0] - previous_time) * food_length <= k:
        current_time = heapq.heappop(food_heap)[0]
        total_time += (current_time - previous_time) * food_length
        food_length -= 1  # 음식 하나가 다 먹었으니 감소
        previous_time = current_time  # 이전 시간을 현재 시간으로 업데이트

    # 남은 음식 중에서 먹어야 할 음식 번호를 계산
    remaining_foods = sorted(food_heap, key=lambda x: x[1])  # 음식 번호 순으로 정렬
    return remaining_foods[(k - total_time) % food_length][1]