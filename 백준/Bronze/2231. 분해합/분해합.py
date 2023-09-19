a = int(input())

lst = []

for i in range(a):
    summ = 0
    plus = 0
    summ += i
    i = str(i)
    for j in range(len(i)):
        plus += int(i[j])
    summ += plus
    if summ == a:
        lst.append(int(i))
if(len(lst) >= 1):
    print(min(lst))
else:
    print(0)