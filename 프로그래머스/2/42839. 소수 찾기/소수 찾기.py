'''
일단 일의자리에 짝수 오면 x
소수 구하는 규칙? 2 ~ n-1로 나눴을 때 나눠떨어지면 안됨
일단 만들 수 있는 숫자 다 구하고 배열 돌면서 하나씩 확인 해야하나
숫자 중복 있으면 안되니까 set 사용
'''

from itertools import permutations

def solution(numbers):
    answer = 0
    arr = []
    for i in numbers:
        arr.append(int(i))
    
    num = set()
    for i in range(1, len(arr)+1):# 1, 2, 3 -> 1 ~ 3
        for j in permutations(arr, i):
            num.add(int(''.join(map(str, j))))
    num = list(num)
    print(num)

    for i in num:
        if i == 0 or i == 1:
            continue
        check = True
        for j in range(2, i):
            if i%j == 0:
                check = False
                break
        if check == True:
            answer += 1
    
    return answer