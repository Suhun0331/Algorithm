import sys

n = int(sys.stdin.readline())

lst = [k for k in range(100001)]

for i in range(1, n+1):
    for j in range(1, i):
        if i-j*j < 0:
            break
        if lst[i] > lst[i-j*j]+1:
            lst[i] = lst[i-j*j]+1
            
print(lst[n])