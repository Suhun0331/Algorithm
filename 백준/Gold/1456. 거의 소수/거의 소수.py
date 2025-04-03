'''
에라토스테네스의 체

1 ~ 10**14 까지의 거의 소수를 다 구하고, 범위 카운팅을 해야 할 듯.

1. 일단 소수 먼저 찾고 나머지는 지움
2. 위 과정에서 찾은 소수를 돌려서 제곱수 다 찾기
3. 입력받은 범위 내에 있는 숫자 개수 세기

---
메모리 초과 남 -> 마지막에 거의 소수 찾을 때 리스트 만들어서 하지 말고
그냥 조건 만족하면 바로 answer += 1 하는 방식으로 수정
'''

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
max = int(b ** 0.5)

prime = [True] * (max+1)

for i in range(2, max//2):
    if prime[i]:
        for j in range(i*i, max+1, i):
            if prime[j]:
                prime[j] = False

answer = 0

for i in range(2, max+1):
    if prime[i]:
        idx = i
        while idx <= b:
            idx *= i
            if idx <= b and idx >= a:
                answer += 1
                    
print(answer)
            





