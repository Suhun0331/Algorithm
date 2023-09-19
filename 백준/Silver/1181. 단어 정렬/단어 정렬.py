num = int(input())

lst = []
for i in range(num):
    a = input()
    if a not in lst:
        lst.append(a)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)