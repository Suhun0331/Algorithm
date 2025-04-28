'''
dp 문제? bfs / dfs?

bfs 사용해서 앞 / 뒤 / x2 해서 들어가려는 초가 기존에 있던
초보다 짧으면 새로 넣음
그게 아니면 q에 안넣고 끝
'''
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

if n >= k:
    print(n-k)
    exit()

count = [100001] * 100001
time = 0
count[n] = time
q = deque()
q.append(n)
current = n
def update(current, time):
    if  0 <= current <= 100000:
        if count[current] > time:
            count[current] = time
            q.append(current)
while q:
    current = q.popleft()
    time = count[current]
    update(current-1, time+1)
    update(current+1, time+1)
    update(current*2, time)
        
print(count[k])
