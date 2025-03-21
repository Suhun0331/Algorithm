'''
큰 배열 하나 만들고 각 칸마다 길이가 3인 배열 만들기
왼 / 가운데 / 오 에서 온 값을 저장하는 것.

어떤 숫자에서 아래로 내려갈 땐 해당 리스트의 왼/오에 저장된 숫자 중
작은 숫자 + 아래에 있는 숫자를 아래의 가운데 칸에 저장

열이 맨 왼쪽/오른쪽일 땐 범위 벗어나지 않게 처리

다 끝나고 맨 아래 저장된 숫자들 중 가장 작은 숫자 반환
'''

import sys
input = sys.stdin.readline

row, col = map(int, input().split())

fuel  = []
for i in range(row):
    fuel.append(list(map(int, input().split())))

dp = [[[0, 0, 0] for _ in range(col)] for _ in range(row)]

for i in range(col):
    for j in range(3):
        dp[0][i][j] = fuel[0][i]

for i in range(1, row):
    dp[i][0][0] = float('inf')
    dp[i][col-1][2] = float('inf')


for i in range(1, row): # 위에서 아래
    for j in range(col): # 왼쪽부터 오른쪽까지
        for k in range(3): # 한 칸에서 왼 / 중 / 오
            if j == 0 and k == 0:
                continue
            if j == col-1 and k == 2:
                continue

            if k == 0:
                dp[i][j][k] = fuel[i][j]+min(dp[i-1][j-1][1], dp[i-1][j-1][2])
            elif k == 1:
                dp[i][j][k] = fuel[i][j]+min(dp[i-1][j][0], dp[i-1][j][2])
            elif k == 2:
                dp[i][j][k] = fuel[i][j]+min(dp[i-1][j+1][0], dp[i-1][j+1][1])         
               

answer = 1e9
for i in range(col):
    #print(dp[row-1][i])
    answer = min(answer, min(dp[row-1][i]))

print(answer)




