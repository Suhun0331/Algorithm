num = int(input())

lst = []
for i in range(num):
    a = int(input())
    lst.append(a)

lst = sorted(lst)
for i in lst:
    print(i)
