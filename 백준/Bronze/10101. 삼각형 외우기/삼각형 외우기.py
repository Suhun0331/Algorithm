lst = []
for i in range(3):
    a = int(input())
    lst.append(a)
    
if sum(lst) == 180:
    if lst[0] == 60 and lst[1] == 60 and lst[2] == 60:
        print("Equilateral")
    elif lst[0] != lst[1] and lst[1] != lst[2] and lst[0] != lst[2]:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")