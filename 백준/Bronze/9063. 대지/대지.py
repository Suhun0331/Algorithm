num = int(input())
lstx=[]
lsty = []

for i in range(num):
    a, b = map(int,input().split())
    lstx.append(a)
    lsty.append(b)


if(num != 0):
    print((max(lstx) - min(lstx)) * (max(lsty) - min(lsty)))
else:
    print(0)