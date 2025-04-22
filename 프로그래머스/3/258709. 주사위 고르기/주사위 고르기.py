'''
모르겠어서 인터넷 찾아봄

combinations 사용해서 a와 b가 가져갈 수 있는 주사위의 조합을 구함
ex) a : 1, 4 - b : 2, 3
product 함수 사용해서 데카르트 곱으로 전체 나올 수 있는 주사위 합 경우 구함
리스트 하나만 정렬하고 bisect써서 경우 별로 이기는 횟수 count

알아갈 부분
1. combinations에서 범위 리스트 만들 때 그냥 range 쓰면 되는 거
2. bisect_left / bisect_right 쓰면 이분탐색 바로 해줌
3. * 연산자 -> 리스트 언패킹 연산자 
-> a = [[1],[2],[3] . . .] 일 때 *a 해주면 [1], [2], [3], . . .로 리스트 까줌
'''
from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    aLists = list(combinations(range(len(dice)), len(dice)//2))
    answer = 0
    result = []
    for aList in aLists:
        bList = []
        for i in range(len(dice)):
            if i not in aList:
                bList.append(i)
        a_case = []
        a_score = []
        for i in aList:
            a_case.append(dice[i])
        for i in product(*a_case):
            a_score.append(sum(i))
            
        b_case = []
        b_score = []
        for i in bList:
            b_case.append(dice[i])
        for i in product(*b_case):
            b_score.append(sum(i))
        b_score.sort()
        cnt = 0
        for i in a_score:
            cnt += bisect_left(b_score, i)
        if answer < cnt:
            answer = cnt
            result = aList
            
    return [i+1 for i in result]
