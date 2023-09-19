while True:
    lst = []
    a, b, c = map(int,input().split())
    if(a == 0 and b == 0 and c == 0):
        break
    lst.append(a)
    lst.append(b)
    lst.append(c)

    if (sum(lst)-max(lst))> max(lst):
        if lst[0] == lst[1] and lst[1] == lst[2] and lst[0] == lst[2]:
            print("Equilateral")
        elif(lst[0] != lst[1] and lst[1] != lst[2] and lst[0] != lst[2]):
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")