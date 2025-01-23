from collections import deque
import sys
n, k = map(int, input().split())

count = [0] * (100001)
visited = [False] * (100001)
visited[n] = True
q = deque()
if n == k:
    print(0)
    sys.exit()

def refact(n, current):
    visited[n] = True
    count[n] = count[current] + 1
    q.append(n)
    
def bfs(start):
    q.append(start)
    while q:
        current = q.popleft()
        if current == k:
            break
        if current + 1 < 100001:
            if not visited[current+1]:
                refact(current+1, current)
        if current - 1 >= 0:
            if not visited[current-1]:
                refact(current-1, current)
        if current*2 < 100001:
            if not visited[current*2]:
                refact(current*2, current)
        
        
bfs(n)
print(count[k])
