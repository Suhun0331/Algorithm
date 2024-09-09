'''
처음에는 가능 불가능을 어떻게 판단해야할지 아예 아이디어 x
-> 아이디어 찾아봄

문제 잘못 이해해서 이상하게 풀다가 .. 정답 코드가 너무 다르길래
문제 다시 읽어보고 알아챔 ..

그 이후 풀이는 그나마 좀 무난 ..? 했던 
'''

from collections import deque
import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())
summ = A+B+C

if summ % 3 != 0:
    print(0)
    sys.exit()

queue = deque([(max(A, B, C), min(A, B, C))])
visit = [[False for i in range(1501)] for j in range(1501)]
visit[max(A, B, C)][min(A, B, C)] = True

while queue:
    a, c = queue.popleft()
    b = summ - a - c

    #print(a, b, c)

    if a == b == c:
        print(1)
        break

    for i, j in [(a, b), (a, c), (b, c)]:
        if i == j:
            continue
        a = i-j
        b = j*2
        c = summ - a - b
        
        max_ = max(a, b, c)
        min_ = min(a, b, c)
        if not visit[max_][min_]:
            visit[max_][min_] = True
            queue.append((max_, min_))

if not(a == b == c):
    print(0)

    

