import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dic = {}

for i in range(n):
    if lst[i] not in dic:
        dic[lst[i]] = 1
    else:
        dic[lst[i]] += 1

m = int(input())

lst2 = list(map(int, input().split()))

for i in range(m):
    if lst2[i] not in dic:
        print(0, end = ' ')
    else:
        print(dic[lst2[i]], end = ' ')
