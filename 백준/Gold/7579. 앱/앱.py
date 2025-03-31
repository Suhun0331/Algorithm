'''
배낭문제 - 생각 못했고 구현 방법 기억 안나서 인터넷 찾아보고 구현방식 복습 후 풂

예제를 예시로 들면, 가로길이는 60 세로길이는 입력받은 개수인 5
하나씩 돌면서 현재 위치의 무게가 60 이하이면 바로 위 가치와 (현재 가치+ 윗줄 중 무게 뺀 가치)의 min값 넣기

dp테이블 초기값은 inf로 다 채우기.

1차 제출 : 메모리 초과 -> 가로축을 줄여야 할 듯 ,, 

gpt한테 물어보고 1차원 배열로 가능한 아이디어 파악함
이전 행만 필요하니까 배열 2개 만들어서 서로 계속 copy 하기.
이 때 dp = dpcopy[:] 로 깊은 복사 사용

2차 제출 : 시간 초과 -> ,,,,

아예 열을 목표 메모리가 아닌 필요한 cost 기준으로 했어야 함.
cost의 범위 0 ~ 100이고 n 또한 0 ~ 100이기 때문에 최악의 경우 10000개의 행 생김 -> 시간 절약

함수화 해서 시간 비교
'''
import copy

n, m = map(int, input().split())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))


def func():
    dp = [[0]*(sum(cost)+1) for _ in range(n+1)]
    answer = sum(cost)+1
    for i in range(1, n+1):
        for j in range(sum(cost)+1):
            if j < cost[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], memory[i] + dp[i-1][j-cost[i]])
            
            if dp[i][j] >= m:
                answer = min(answer ,j)
    return answer
    # for i in dp:
    #     print(i)
    # print()
print(func())
            
    
