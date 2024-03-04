a = int(input())

lst = []

for i in range(a):
    lst.append(input())
lst = sorted(lst)
lst = sorted(lst, key = len)

print(lst[0])
for i in range(1, len(lst)):
    if lst[i] != lst[i-1]:
        print(lst[i])
