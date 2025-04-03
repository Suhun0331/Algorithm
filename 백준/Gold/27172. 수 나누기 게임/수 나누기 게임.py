'''
풀이 보고 풀었음

3 -> 12 하면 3이 점수를 받음 -> 12가 점수를 받을 때 3도 받는다는 뜻.
큰 수부터 체인 형식으로 계산하면 되지 않을까 ..?
ex) 12가 5점인데 3 -> 12 ok니까 3은 (5점 + 1)
--------
에라토스테네스의 체 -> 소수 찾기
2의 배수 다 지움 -> 3의 배수 다 지움 -> 5의 배수 다 지움 -> . . .
이렇게 남은 소수의 배수를 다 지워나감으로써 끝까지 반복해서 소수를 찾는 방식

위 방식 응용 
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max = 1000001
numlist = [-1] * (max)
for idx, i in enumerate(arr):
    numlist[i] = idx

score = [0] * n

for i in range(max):
    if numlist[i] > -1:
        for j in range(i, max, i):
            if numlist[j] > -1:
                score[numlist[i]] += 1
                score[numlist[j]] -= 1

print(*score)