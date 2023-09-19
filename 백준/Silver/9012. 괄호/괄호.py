n = int(input())
for i in range(n):
    a = list(input())
    lst = []
    
    check = 0
    for j in range(len(a)):
        if a[j] == '(':
            lst.append(a[j])
        elif a[j] == ')':
            if len(lst) != 0:
                lst.pop()
            else:
                check = 1
                break
    if check == 0 and len(lst) == 0:
        print("YES")
    else:
        print("NO")