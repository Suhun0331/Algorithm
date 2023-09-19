import sys
from collections import Counter

num = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))
stack = []
answer = [-1]*num

freq = Counter(lst)

for i in range(num):
    while stack and freq[lst[stack[-1]]] < freq[lst[i]]:
        answer[stack.pop()] = lst[i]
        
    stack.append(i)

for i in answer:
    print(i, end = ' ')