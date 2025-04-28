'''
dp 문제? bfs / dfs?

bfs 사용해서 앞 / 뒤 / x2 해서 들어가려는 초가 기존에 있던
초보다 짧으면 새로 넣음
그게 아니면 q에 안넣고 끝
+
시간 줄이기 -> *2의 경우 appendleft 해서 먼저 처리 
'''
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

if n >= k:
    print(n-k)
    exit()

count = [-1] * 100001
time = 0
count[n] = time
q = deque()
q.append(n)

while q:
    current = q.popleft()
    if current == k:
        break
    time = count[current]
    if current * 2 <= 100000 and count[current*2] == -1:
        count[current*2] = time
        q.appendleft(current*2)
    if current-1 >= 0 and count[current-1] == -1:
        count[current-1] = time+1
        q.append(current-1)
    if current + 1 <= 100000 and count[current+1] == -1:
        count[current+1] = time+1
        q.append(current+1)
    
        
print(count[k])