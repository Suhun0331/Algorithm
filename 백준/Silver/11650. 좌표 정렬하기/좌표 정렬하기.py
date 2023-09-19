num = int(input())

lst = []
for i in range(num):
    a, b = map(int,input().split())
    lst.append([a, b])
lst.sort()

for i in range(len(lst)):
    print(lst[i][0], lst[i][1])