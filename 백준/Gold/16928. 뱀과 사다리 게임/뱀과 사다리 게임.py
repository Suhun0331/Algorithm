from collections import deque

a, b = map(int, input().split())

trap = [0] * 101
visit = [False] * 101
for i in range(a+b):
    start, end = map(int, input().split())
    trap[start] = end

queue = deque()
queue.append(1)
visit[1] = True
move = [0] * 101
move[1] = 0

while queue:
    current = queue.popleft()
    for i in range(1, 7):
        if current + i <= 100:
            next = current + i
        else:
            continue
        if trap[next] != 0:
            next = trap[next]
        if visit[next] == True:
            continue
        queue.append(next)
        visit[next] = True
        move[next] = move[current] + 1
    if visit[100] == True:
        break

print(move[100])

