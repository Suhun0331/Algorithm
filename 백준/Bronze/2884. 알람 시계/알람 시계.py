a, b = map(int, input().split())

b -= 45

if(a == 0 and b<0):
    a = 23
    b += 60
    print(a, b)
elif(a != 0 and b<0):
    a -=1
    b += 60
    print(a, b)
else:
    print(a,b)