import sys
n = int(sys.stdin.readline())

cost = list(map(int, sys.stdin.readline().split()))
maxx = [0]*(n+1)
cost.insert(0,0)

for i in range(1, n+1):
    if i == 1:
        maxx[i] = cost[i]
    else:
        maxx[i] = cost[i]
        for j in range(1, i//2+1):
            if maxx[i]<maxx[j]+maxx[i-j]:
                maxx[i] = maxx[j]+maxx[i-j]
                

print(maxx[n])