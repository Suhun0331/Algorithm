'''
치킨집 좌표를 먼저 다 구하고, 각 치킨집 별 집마다 치킨거리 구하기
<집 순서대로 치킨거리 구한거>
[1 5 7] - 치킨집 1
[5 2 1]
[4 4 7]
[1 1 1] - 치킨집 4

m이 3일 때 1개를 순서대로 빼면서 각 리스트 인덱스의 최솟값 구해서 더하면
그게 도시의 치킨거리
이걸 다 구해서 min값 구하기?

'''
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append([i, j])
        elif arr[i][j] == 1:
            house.append([i, j])

alive = list(combinations(chicken, m))
dist = 0
x, y = 0, 0
minn = 10000
check_dist = []
ans = 0

for i in alive:
    for j in house:
        for k in i:
            x, y = abs(k[0] - j[0]), abs(k[1] - j[1])
            dist = (x+y)
            check_dist.append(dist)
        ans += min(check_dist)
        check_dist.clear()
    minn = min(minn, ans)
    ans = 0


print(minn)
