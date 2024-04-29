import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int,input().split())
tree = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in tree:
        tree[a] = []
    if b not in tree:
        tree[b] = []
    tree[a].append(b)
    tree[b].append(a)

for key in tree:
    tree[key].sort()

visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)

    print(node, end = ' ')

    for i in tree[node]:
        dfs(i)
        
visited2 = set()

def bfs(start):
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node in visited2:
            continue

        visited2.add(node)
        print(node, end = ' ')
        
        for i in tree[node]:
            if i not in visited2:
                queue.append(i)

if v not in tree:
    print(v)
    print(v)
    exit()
    
dfs(v)
print()
bfs(v)
