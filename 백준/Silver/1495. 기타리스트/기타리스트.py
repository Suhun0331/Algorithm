n, s, m = map(int, input().split())
vol = list(map(int, input().split()))
arr = [[0]*(m+1) for _ in range(n)]

for i in range(n):
    for j in range(m+1):
        if i == 0:
            if s - vol[i] >= 0:
                arr[i][s - vol[i]] = 1
            if s + vol[i] <= m:
                arr[i][s + vol[i]] = 1
        else:
            if arr[i-1][j] == 1:
                if j+vol[i] <= m:
                    arr[i][j+vol[i]] = 1
                if j - vol[i] >= 0:
                    arr[i][j-vol[i]] = 1
maxx = -1
for i in range(m+1):
    if arr[n-1][i] == 1:
        maxx = i

print(maxx)
        
