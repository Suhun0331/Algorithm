import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dup = set()

for i in range(n):
    dup.add(lst[i])

m = int(input())

lst2 = list(map(int, input().split()))

for i in range(m):
    if lst2[i] in dup:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
