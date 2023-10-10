import sys

n = int(sys.stdin.readline())

lst = [0]*1001

def df(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if lst[n] != 0:
        return lst[n]
    else:
        lst[n] = (df(n-1) + df(n-2))%10007
        return lst[n]
print(df(n))