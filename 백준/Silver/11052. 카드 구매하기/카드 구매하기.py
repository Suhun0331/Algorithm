n = int(input())
lst = [0]*(n+1)
maxx = [0] * (n+1)

lst = list(map(int, input().split()))
lst.insert(0,0)
for i in range(1, n+1):
    if i == 1:
        maxx[i] = lst[i]
    else:
        maxx[i] = lst[i]
        for j in range(1, i//2+1):
            if maxx[i] < maxx[j]+maxx[i-j]:
                maxx[i] = maxx[j]+maxx[i-j]
print(maxx[n])