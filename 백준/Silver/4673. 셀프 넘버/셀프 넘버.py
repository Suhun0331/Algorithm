check = [False] * 10001

for i in range(1, 10000):
    add = i
    for j in str(i):
        add += int(j)
    if add <= 10000:
        check[add] = True
    add = 0

for i in range(1, 10001):
    if check[i] == False:
        print(i)
