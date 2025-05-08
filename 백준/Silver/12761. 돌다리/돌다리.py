from collections import deque


def solution(start):
    q = deque()
    q.append(start)
    graph[start] = 0

    while q:
        l = q.popleft()
        for i in (l - 1, l + 1, l - a, l + a, l - b, l + b, l * a, l * b):
            if 0 <= i <= 100000 and graph[i] == -1:
                q.append(i)
                graph[i] = graph[l] + 1
            if i == m:
                print(graph[m])
                exit()


a, b, n, m = map(int, input().split())
graph = [-1] * 100001
solution(n)