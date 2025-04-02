'''
2xn 타일이랑 비슷한 유형으로 풀기(dp)
행렬 하나씩 추가될 때마다 min(기존꺼 + 새로운 행렬, 기존꺼-1 + 이전꺼+새로운 행렬)로 새로운 값 갱신
-> 틀림

방식 아예 모르겠어서 인터넷 찾아봄
풀었던 dp중에 제일 어렵다 ... 
아니 그냥 지금까지 풀었던 모든 문제중에 젤 어렵 .. 아직도 이해 확실히 안감
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*(n) for _ in range(n)]

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, n-i):
        if i == 1:
            dp[j][j+i] = mat[j][0] * mat[j][1] * mat[j+i][1]
            continue
        dp[j][j+i] = float('inf')
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + mat[j][0]*mat[k][1]*mat[j+i][1])
# print(dp)
print(dp[0][-1])
        


        