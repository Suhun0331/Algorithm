'''
행 단위로 확인
왼쪽부터 가면서 1을 만나면 start, 오른쪽으로 가다가 또 1을 만나면
그 사이는 다 물 고임.
오른쪽으로 갈 때 0이면 물 고일 후보 += 1, 1이면 물 고일 후보 0
벽 만나면 다음 행.
'''
h, w = map(int, input().split()) #(h, w)
water = list(map(int, input().split()))

block = [[0] * w for _ in range(h)]
width = 0
for i in water: # 3 0 1 4
    for j in range(i):# 0 1 2
        block[h-j-1][width] = 1
    width += 1

answer = 0

for i in range(h):
    check = False
    sub = 0
    for j in range(w): # (i, j)
        if block[i][j] == 1 and check:
            answer += sub
            sub = 0
        elif block[i][j] == 1 and not check:
            check = True
        elif block[i][j] == 0 and check:
            sub += 1
        elif block[i][j] == 0 and not check:
            continue
print(answer)