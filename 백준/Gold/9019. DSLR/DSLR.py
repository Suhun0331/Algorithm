'''
계속 시간초과 나길래 대체 어떻게 더 줄여 했는데
pypy로 했어야했다
하ㅏㅏㅏㅏㅏㅏㅏㅏ 내 시간;;;
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

command = ['D', 'S', 'L', 'R']

for i in range(n):
    queue = deque()
    record = ['']*10001
    visit = [False] * 10001
 
    start, end = map(int, input().split())
    queue.append(start)
    visit[start] = True

    while queue:
        substart = queue.popleft()
        
        if substart == end:
            print(record[end])
            break

        sub = (substart*2)%10000
        if not visit[sub]:
            visit[sub] = True
            queue.append(sub)
            record[sub] = record[substart] + 'D'

        if substart == 0:
            sub = 9999
        else:
            sub = substart - 1
        if not visit[sub]:
            visit[sub] = True
            queue.append(sub)
            record[sub] = record[substart] + 'S'


        sub = substart // 1000 + (substart % 1000)*10
        if not visit[sub]:
            visit[sub] = True
            queue.append(sub)
            record[sub] = record[substart] + 'L'

        sub = substart // 10 + (substart % 10) * 1000
        if not visit[sub]:
            visit[sub] = True
            queue.append(sub)
            record[sub] = record[substart] + 'R'


