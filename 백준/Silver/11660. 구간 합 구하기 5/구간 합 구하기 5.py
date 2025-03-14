'''
도넛과 막대그래프

값 입력받고 그때 for문써서 하면 너무 오래걸림
맨 앞 ~ 맨 뒤 하면 10만 x 10만 돼버림
누적합 써야함.

행 별 누적합 구하면 될 듯
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

sumarr = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            sumarr[i][j] = arr[i][j]
        elif i == 0:
            sumarr[i][j] = sumarr[i][j-1]+arr[i][j]
        elif j == 0:
            sumarr[i][j] = sumarr[i-1][j] +arr[i][j]
        else:
            sumarr[i][j] = sumarr[i-1][j] + sumarr[i][j-1] - sumarr[i-1][j-1]+arr[i][j]

for i in range(m):
    answer = 0
    x1, y1, x2, y2 = map(int, input().split())
    
    if (x1, y1) == (x2, y2):
        answer = arr[x1-1][y1-1]
    elif x1 == 1 and y1 == 1:
        answer = sumarr[x2-1][y2-1]
    elif x1 == 1:
        answer = sumarr[x2-1][y2-1] - sumarr[x2-1][y1-2]
    elif y1 == 1:
        answer= sumarr[x2-1][y2-1] - sumarr[x1-2][y2-1]
        #print(sumarr[x2-1][y2-1], sumarr[x1-2][y2-1])
    else:
        answer = sumarr[x2-1][y2-1]-sumarr[x1-2][y2-1]-sumarr[x2-1][y1-2]+sumarr[x1-2][y1-2]
    print(answer)

    
