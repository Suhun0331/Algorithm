import sys
n = int(sys.stdin.readline())

cost = [0] + list(map(int, sys.stdin.readline().split()))
minn = [0]*(n+1)


for i in range(1, n+1):
    if i == 1:
        minn[i] = cost[i]
    else:
        minn[i] = cost[i]
        for j in range(1, i//2+1):
            if minn[i]>minn[j]+minn[i-j]:
                minn[i] = minn[j]+minn[i-j]
                

print(minn[n])