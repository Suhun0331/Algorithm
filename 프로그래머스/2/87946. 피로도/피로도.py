'''
어떤 순서로 탐험을 해야할지 먼저 생각.
1. 필요 피로도 순 or 소모 피로도 순 정렬?
필요 피로도 순으로 해야 놓치지 않을 거 같긴 한데
모든 순서 경우의 수 다 구하기?

그냥 dfs로 하나씩 다 들어가면서 더이상 들어가지 못하면 현재 count를 answer에 초기화

1. 순열로 모든 경우 구하기
2. dfs사용하기
'''
from itertools import permutations

def solution(k, dungeons):
    turn = list(permutations(range(len(dungeons))))
    answer = 0
    for i in turn:
        piro = k
        count = 0
        for idx in i:
            if piro >= dungeons[idx][0]:
                piro -= dungeons[idx][1]
                count += 1
            else:
                break
        answer = max(answer, count)
        
    return answer
    
    
    