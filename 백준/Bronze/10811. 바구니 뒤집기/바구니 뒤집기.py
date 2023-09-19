a, b = map(int, input().split())

result = [i for i in range(1, a+1)]

for i in range(b):
    c, d = map(int, input().split())
    result[c-1:d] = reversed(result[c-1:d])
    
for i in result:
    print(i, end = " ")