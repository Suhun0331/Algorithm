arr = []
for i in range(30):
    arr.append(i+1)
for i in range(28):
    a = int(input())
    arr.remove(a)
for i in arr:
    print(i)