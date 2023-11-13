n = int(input())

lst = [0] * 11

for i in range(1, 11):
    if i == 1:
        lst[i] = 1
    elif i == 2:
        lst[i] = 2
    elif i == 3:
        lst[i] = 4
    else:
        lst[i] = lst[i-1]+lst[i-2]+lst[i-3]
for i in range(n):
    num = int(input())
    print(lst[num])