import sys
from collections import deque

n = int(sys.stdin.readline())

lst = deque([i for i in range(1, n+1)])


while(len(lst) != 1):
    lst.popleft()
    tmp = lst.popleft()
    lst.append(tmp)
print(lst[0])
