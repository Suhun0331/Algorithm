a = list(input())

answer = []

for i in range(len(a)):
    strr = ''
    for j in a:
        strr += j
    answer.append(strr)
    del a[0]
    
answer.sort()
for i in answer:
    print(i)