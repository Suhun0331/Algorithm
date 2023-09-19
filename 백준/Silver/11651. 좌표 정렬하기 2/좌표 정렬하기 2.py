num = int(input())

lst = []
for i in range(num):
    a, b = map(int,input().split())
    lst.append([b, a])
lst.sort()

for i in range(len(lst)):
    print(lst[i][1], lst[i][0])