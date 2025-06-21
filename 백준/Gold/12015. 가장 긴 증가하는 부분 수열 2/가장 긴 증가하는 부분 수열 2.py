import sys
import bisect as bi

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
uplist = []

for i in arr:
    idx = bi.bisect_left(uplist, i)
    if idx == len(uplist):
        uplist.append(i)
    else:
        uplist[idx] = i
print(len(uplist))