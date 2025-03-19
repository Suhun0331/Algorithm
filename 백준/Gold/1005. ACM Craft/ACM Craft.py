'''
위상정렬 이용
숫자 하나 뺄 때마다 q에 다음 숫자들이 쌓임.

한 번 다 쌓은 후에 만약 그 쌓인 q 안에 목표 숫자가 있으면,
지금 시간 + 목표숫자 걸리는 시간
없으면 q 안에 있는 목표 숫자들 중 가장 오래 걸리는 시간을 현재 시간에 +

@@@
위 방식 썼더니 시간 중복 계산 해결이 안됨.

시간 중복 계산 처리하는 방식 모르겠어서 gpt한테 물어보고
dp 배열 이용해야 한다는 아이디어 힌트 받음.

'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    time.insert(0, 0)
    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    answer = time[1]
    q = deque()
    dp = [0] * (n+1)

    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    target = int(input())

    for i in range(1, n+1):
        if indegree[i] == 0:
            dp[i] = time[i]
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i])
            if indegree[i] == 0:
                q.append(i)
    print(dp[target])

