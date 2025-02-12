'''
그냥 순열로 모든 경우의 수 구해서 각각 answer 구하기?
중간에 충족 안되면 break
'''
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    perm = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    
    for i in perm:
        copy = k
        count = 0
        for j in i: # 0, 1, 2
            if copy < dungeons[j][0]:
                answer = max(answer, count)
                break
            count += 1
            copy -= dungeons[j][1]
            if j == i[-1]:
                return len(i)
    
    
    return answer