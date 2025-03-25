'''
처음에는 유니온파인드 생각했는데 아닌 거 같았음
dfs인 거 같았는데 중간 처리가 복잡해서 인터넷에서 힌트 얻음

그 후에도 재귀 리밋 풀어줘야하는거 까먹어서 찾아봄
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def dfs(n):
    global answer
    cos.append(n)
    visited[n] = True
    if not visited[arr[n]]:
        dfs(arr[n])
    else:
        if arr[n] in cos:
            answer -= (len(cos)-cos.index(arr[n]))
        else:
            return

for _ in range(T):
    n = int(input())
    answer = n
    graph = [0]*(n+1)
    visited = [False] * (n+1)
    cos = []
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    for i in range(1, n+1):
        if not visited[i]:
            cos = []
            dfs(i)
    print(answer)
