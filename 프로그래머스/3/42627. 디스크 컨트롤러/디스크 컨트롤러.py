import heapq as hq

def solution(jobs):
    heap = []
    jobs.sort(key=lambda x: x[0])  # 요청 시간 기준 정렬
    now = 0         # 현재 시간
    finish = 0      # 완료된 작업 수
    answer = 0      # 총 대기 시간 누적
    idx = 0         # jobs에서 아직 힙에 넣지 않은 작업의 인덱스

    while finish < len(jobs):
        # 현재 시간까지 들어온 작업들을 힙에 추가
        for job in jobs[idx:]:
            if now >= job[0]:
                hq.heappush(heap, (job[1], job[0]))  # (소요시간, 요청시간, 인덱스)
                idx += 1

        if heap:
            # 가장 짧은 작업부터 수행
            time, start = hq.heappop(heap)
            print(time, start)  # 디버깅용 출력
            now += time
            answer += (now - start)  # 요청부터 종료까지 걸린 시간 누적
            finish += 1
        else:
            # 수행할 작업이 없으면 시간 1 증가
            now += 1

    return answer // len(jobs)  # 평균 작업 시간 반환
