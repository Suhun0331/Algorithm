num = int(input())

lst = []
for i in range(num):
    a, b = map(str, input().split())
    a = int(a)
    lst.append([a, b])

lst.sort(key = lambda x : x[0])

for i in range(num):
    print(lst[i][0], lst[i][1])