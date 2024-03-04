lst = []
for i in range(9):
    lst.append(int(input()))
check = 0
for i in range(8):
    for j in range(i+1, 9):
        if (sum(lst) - lst[i] - lst[j]) == 100:
            del lst[j]
            del lst[i]
            check = 1
            break
    if check == 1:
        break
lst = sorted(lst)
for i in lst:
    print(i)
