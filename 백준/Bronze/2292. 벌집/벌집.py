a = int(input())
num = 1
suc = 1

while True:
    if(a>num):
        num +=6*suc
        suc +=1
    else:
        print(suc)
        break