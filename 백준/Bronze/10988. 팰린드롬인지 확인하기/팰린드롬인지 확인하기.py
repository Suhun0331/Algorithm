a = list(input())
check = True

b = len(a)//2
for i in range(b):
    if(a[i] != a[len(a)-i-1]):
       check = False

if check:
       print("1")
else:
    print("0")