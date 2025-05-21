'''
1520 내리막길
1차 제출 -> 시간초과
출력이 10억 이하의 정수라는 거 보면 경우의 수가 많아서 일반적인 dfs로는 안됨

dp까지 추가해야 할 듯.

dp 추가하는 방식은 gpt 검색.
**visited 굳이 안쓰고 dp -1로 초기화 함으로써 두가지 기능 동시에 수행할 수 있음**
'''
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

m, n = map(int, input().split()) # (m, n)
mapp = []
count = 0
visited = [[False]*n for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dp = [[-1] * n for _ in range(m)]

for _ in range(m):
    mapp.append(list(map(int, input().split())))

def dfs(cm, cn):

    if dp[cm][cn] != -1:
        return dp[cm][cn]
    
    if (cm, cn) == (m-1, n-1):
        return 1

    dp[cm][cn] = 0
    
    for i in range(4):
        nm, nn = cm+dx[i], cn+dy[i]
        if 0<=nm<len(mapp) and 0<=nn<len(mapp[0]):
            if mapp[nm][nn] < mapp[cm][cn]:
                dp[cm][cn] += dfs(nm, nn)
    return dp[cm][cn]
        

print(dfs(0, 0))
