a = int(input())
b = int(input())
lst = []
for i in range(a, b+1):
    lst.append(i)

for i in range(a, b+1):
    for j in range(2, i):
        if(i % j == 0):
            lst.remove(i)
            break
if 1 in lst:
    lst.remove(1)
    
if(len(lst) == 0):
    print("-1")
else:
    print(sum(lst))
    print(min(lst))