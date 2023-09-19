aa, bb = map(int, input().split())

lst = []
count = []

for i in range(aa):
    lst.append(input())

for i in range(aa-7):
    for j in range(bb-7):
        w = 0
        b = 0
        for k in range(i,i+8):
            for q in range(j, j+8):
                if (k+q) %2 == 0:
                    if(lst[k][q] == 'W'):
                        b += 1
                    else:
                        w += 1
                else:
                    if(lst[k][q] == 'B'):
                        b += 1
                    else:
                        w += 1 
        count.append(w)
        count.append(b)
print(min(count))