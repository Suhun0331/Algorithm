a = []
b = []

n, m = map(int,input().split())

for i in range(n):
    num = list(map(int, input().split()))
    a.append(num)

for i in range(n):
    num = list(map(int, input().split()))
    b.append(num)

for i in range(n):
    for j in range(m):
        sum = a[i][j]+b[i][j]
        print(sum, end = ' ')
    print()