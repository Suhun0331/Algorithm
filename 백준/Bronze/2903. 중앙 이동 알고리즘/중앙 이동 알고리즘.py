a = int(input())
n = 2
plus = 1
for i in range(a):
    n += plus
    plus *= 2
print(n*n)