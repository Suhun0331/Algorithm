import sys

a = int(input())
lst = []
for i in range(a):
    lst.append(int(sys.stdin.readline()))
lst.sort()
for i in range(a):
    print(lst[i])