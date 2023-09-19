a = []
maxx = 0
max_1 = 0
max_2 = 0

for i in range(9):
    num = list(map(int, input().split()))
    a.append(num)

for i in range(9):
    for j in range(9):
        if(a[i][j] > maxx):
            maxx = a[i][j]
            max_1 = i
            max_2 = j
print(maxx)
print("{} {}".format(max_1+1, max_2+1))