'''
소수 -> 2부터 본인//2 까지 나누어떨어지지 않으면 소수

흩어진 숫자들로 하나의 숫자 만들기 -> dfs?
순열 사용해서 모든 경우의 수 뽑고 그거 int로 만들기
'''
from itertools import permutations

def solution(numbers):
    count = 0
    numlst = set()
    
    for i in range(1, len(numbers)+1):
        lst = list(permutations(list(numbers), i))
        for j in lst:
            number = int(''.join(j))
            numlst.add(number)
    # print(numlst)
    for i in numlst:
        sosu = True
        if i == 1 or i == 0:
            continue
        for j in range(2, i//2+1):
            if i%j == 0:
                sosu = False
                break
        if sosu:
            count += 1
    return count
    
    
    
    
    