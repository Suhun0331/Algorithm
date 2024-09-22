n = int(input())
connect = int(input())

tree = {}
for i in range(1, n+1):
    tree[i] = []
    
for i in range(connect):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

visited = set()
cnt = -1
def dfs(node):
    global cnt
    if node in visited:
        return
    #print(node)
    visited.add(node)
    cnt += 1
    for i in tree[node]:
        dfs(i)

dfs(1)

print(cnt)


