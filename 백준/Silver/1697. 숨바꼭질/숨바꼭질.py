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
    
def bfs(start):
    q.append(start)
    while q:
        current = q.popleft()
        if current == k:
            break
        if current + 1 < 100001:
            if not visited[current+1]:
                visited[current+1] = True
                count[current+1] = count[current] + 1
                q.append(current+1)
        if current - 1 >= 0:
            if not visited[current-1]:
                visited[current-1] = True
                count[current-1] = count[current] + 1
                q.append(current-1)
        if current*2 < 100001:
            if not visited[current*2]:
                visited[current*2] = True
                count[current*2] = count[current] + 1
                q.append(current*2)
        
        
bfs(n)
print(count[k])
            
    

