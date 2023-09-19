a = int(input())
count = a

for i in range(a):
    sen = list(input())

    for j in range(len(sen)-1):
        if(sen[j] == sen[j+1]):
            continue
        elif(sen[j] in sen[j+1:]):
            count -=1
            break
print(count)