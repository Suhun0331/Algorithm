list = []

for i in range(1,31):
    list.append(i)
    
for i in range(28):
    a = int(input())
    list.remove(a)

list.sort()
print(list[0])
print(list[1])