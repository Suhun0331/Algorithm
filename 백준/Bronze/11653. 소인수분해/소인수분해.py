a = int(input())
lst = []
while a != 1:
    for i in range(2, a+1):
        if(a%i == 0):
            a = a//i
            lst.append(i)
            break
for i in lst:
    print(i)