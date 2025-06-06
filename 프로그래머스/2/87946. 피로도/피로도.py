'''
어떤 순서로 탐험을 해야할지 먼저 생각.
1. 필요 피로도 순 or 소모 피로도 순 정렬?
필요 피로도 순으로 해야 놓치지 않을 거 같긴 한데
모든 순서 경우의 수 다 구하기?

그냥 dfs로 하나씩 다 들어가면서 더이상 들어가지 못하면 현재 count를 answer에 초기화

1. 순열로 모든 경우 구하기
2. dfs사용하기
'''
def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0
    def dfs(count, piro):
        nonlocal answer
        answer = max(answer, count)
        for i in range(len(dungeons)):
            if not visited[i] and piro >= dungeons[i][0]:
                visited[i] = True
                dfs(count + 1, piro-dungeons[i][1])
                visited[i] = False
    dfs(0, k)
    return answer