'''
알고리즘 : 누적합 
입력받는 수의 개수가 너무 커서 특정 수 바뀌었을 때 그 오른쪽 누적합 다 바꾸는건 불가능

1. 처음 수를 입력받아서 누적합 리스트 생성 -> 100만
2. 구간 합을 구하기 전 숫자 바뀌는 부분들 체크 ..?
or 구간 합 구해야 할 때, 그 구간 안에 기존에 바뀐 숫자들이 있다면 (구간합 - 변동값)

바뀐 숫자들 저장된 리스트 만들고, 누적합 구할 때마다 해당 리스트 다 돌면서 구간 안에 있는지 확인,
구간 안에 있으면 그만큼 (구간합-변동값)

만약 바뀐 숫자가 리스트 안에 있으면(기존에 이미 바뀐 적 있는 값이면), 하나만 남기기?

구간이 3 ~ 10이면, 10 이전에 있는 바뀐 숫자값 다 반영해야함.
2가 바뀌었어도 누적합이 바뀌기 때문에 반영 해줘야함. 
1차 제출 -> 시간초과 
'''
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
num = [0]
sumlst = [0] * (n+1)
change_num = [0] * (n+1)
change_idx = set()
for i in range(n):
    num.append(int(input()))
for i in range(1, n+1):
    sumlst[i] = sumlst[i-1] + num[i]

for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        change_idx.add(b)
        change_num[b] = c
    elif a == 2:
        answer = sumlst[c] - sumlst[b-1]
        for i in change_idx:
            if b <= i <= c:
                answer += (change_num[i] - num[i])
        print(answer)
