number = int(input())
lst = [25, 10, 5, 1]
count = [0, 0, 0, 0]


for i in range(number):
    money = int(input())
    cnt = 0
    for j in lst:
        num = money // j
        count[cnt] = num
        money %= j
        cnt += 1

    print(' '.join(map(str,count)))