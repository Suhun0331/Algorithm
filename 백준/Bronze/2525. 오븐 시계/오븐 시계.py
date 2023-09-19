a, b = map(int, input().split())
c = int(input())

b += c

if(b < 60):
    print(a, b)
elif(b >= 60 and a == 23):
    a = (a+(b//60)) - 24
    b = b%60
    print(a, b)
elif(b >= 60 and a != 23):
    a += b//60
    b = b%60
    if(a < 24):
        print(a, b)
    else:
        a = (a+(b//60)) - 24
        print(a, b)