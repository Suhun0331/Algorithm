import sys
input = sys.stdin.readline

def find(parent, n):
    if parent[n] != n:
        parent[n] = find(parent, parent[n])
    return parent[n]

def union(parent, n1, n2):
    a = find(parent, n1)
    b = find(parent, n2)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    costs = []
    answer = 0
    parent = [i for i in range(n+1)]
    for i in range(m):
        costs.append(list(map(int, input().split())))


    costs.sort(key = lambda x: x[2])

    for i in costs:
        n1, n2, cost = i
        if find(parent, n1) != find(parent, n2):
            union(parent, n1, n2)
        else:
            answer += cost

    print(answer)




