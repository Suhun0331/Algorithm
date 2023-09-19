a = []
b = []
count = 0
for i in range(100):
    for j in range(100):
        b.append(0)
    a.append(b)
    b = []

num = int(input())
for i in range(num):
    aa, bb = map(int,input().split())
    for h in range(10):
        for w in range(10):
            a[aa+h][bb+w] = 1


for i in range(100):
    for j in range(100):
        if(a[i][j] == 1):
            count += 1

print(count)