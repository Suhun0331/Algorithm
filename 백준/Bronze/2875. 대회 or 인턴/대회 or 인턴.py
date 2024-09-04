n, m, k = map(int, input().split())

for i in range(k):
    if n > m*2:
        n -= 1
    else:
        m -= 1
#print(n, m)
a = n // 2
b = m // 1
#print(a, b)

print(min(a, b))
