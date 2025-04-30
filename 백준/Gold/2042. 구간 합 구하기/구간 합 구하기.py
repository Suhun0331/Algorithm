import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

num = [0]  # 1-based indexing
sumlst = [0] * (n + 1)

for _ in range(n):
    num.append(int(input()))

# 누적합 계산
for i in range(1, n + 1):
    sumlst[i] = sumlst[i - 1] + num[i]

change_map = {}  # 변경된 인덱스와 변경된 값 기록

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        change_map[b] = c  # b번째 값을 c로 수정
    elif a == 2:
        # 기본 누적합
        result = sumlst[c] - sumlst[b - 1]
        # 변경된 값 반영
        for i in change_map:
            if b <= i <= c:
                # 누적합엔 기존 num[i]가 반영되어 있고, 지금은 c로 바뀐 상황
                result += (change_map[i] - num[i])
        print(result)
