'''
첫번째 풀이. 혼자 풀긴 했는데 코드가 너무 많이 중복됨. 맞으면 코드 길이 줄이는 법 찾기
'''
import sys
input = sys.stdin.readline

n = int(input())
inf = float('inf')
rdp = [[inf]*3 for _ in range(n)]
gdp = [[inf]*3 for _ in range(n)]
bdp = [[inf]*3 for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    if i == 0:
        rdp[0][0] = arr[0][0]
        gdp[0][1] = arr[0][1]
        bdp[0][2] = arr[0][2]
        # print(rdp)
        # print(gdp)
        # print(bdp)
        # print()
        continue
    if i == 1:
        rdp[1][1] = rdp[0][0] + arr[1][1]
        rdp[1][2] = rdp[0][0] + arr[1][2]
        gdp[1][0] = gdp[0][1] + arr[1][0]
        gdp[1][2] = gdp[0][1] + arr[1][2]
        bdp[1][1] = bdp[0][2] + arr[1][1]
        bdp[1][0] = bdp[0][2] + arr[1][0]
        continue
    for j in range(3):
        if j == 0:
            rdp[i][j] = min(rdp[i-1][1], rdp[i-1][2]) + arr[i][j]
            gdp[i][j] = min(gdp[i-1][1], gdp[i-1][2]) + arr[i][j]
            bdp[i][j] = min(bdp[i-1][1], bdp[i-1][2]) + arr[i][j]
        elif j == 1:
            rdp[i][j] = min(rdp[i-1][0], rdp[i-1][2]) + arr[i][j]
            gdp[i][j] = min(gdp[i-1][0], gdp[i-1][2]) + arr[i][j]
            bdp[i][j] = min(bdp[i-1][0], bdp[i-1][2]) + arr[i][j]
        elif j == 2:
            rdp[i][j] = min(rdp[i-1][1], rdp[i-1][0]) + arr[i][j]
            gdp[i][j] = min(gdp[i-1][1], gdp[i-1][0]) + arr[i][j]
            bdp[i][j] = min(bdp[i-1][1], bdp[i-1][0]) + arr[i][j]
    # print(rdp)
    # print(gdp)
    # print(bdp)
    # print()
    rdp[-1][0] = inf
    gdp[-1][1] = inf
    bdp[-1][2] = inf

print(min(min(rdp[-1]), min(gdp[-1]), min(bdp[-1])))