import sys

n = int(sys.stdin.readline())

lst = [0]*(n+1)


for i in range(2, n+1):

    if i%2 == 0 and i%3 == 0:
        lst[i] = min(lst[i//2],lst[i//3], lst[i-1])+1
    elif i%3 == 0:
        lst[i] = min(lst[i//3], lst[i-1])+1
    elif i%2 == 0:
        lst[i] = min(lst[i//2], lst[i-1])+1
    else:
        lst[i] = lst[i-1]+1
    

print(lst[n])