while True:
    a = int(input())
    if(a == -1):
        break
    lst = []
    for i in range(1, a):
        if(a%i == 0):
            lst.append(i)
    
    if(sum(lst) == a):
        print(a , "=" , " + ".join(str(i) for i in lst))
    else:
        print("%d is NOT perfect."%a)