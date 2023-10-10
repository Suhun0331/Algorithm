import sys
n = int(sys.stdin.readline())

lst = [0]*1001
for i in range(1,1001):
    if i == 1:
        lst[i] = 1
    if i == 2:
        lst[i] = 3
    if i>=3:
        lst[i] = (lst[i-1] + 2*lst[i-2])%10007
print(lst[n])