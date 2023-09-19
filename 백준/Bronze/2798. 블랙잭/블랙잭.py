a, b = map(int,input().split())

lst = list(map(int,input().split()))

lst_max = []

summ = 0

for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1, a):
            summ = lst[i] + lst[j] + lst[k]
            if(summ <= b):
                lst_max.append(summ)
                summ = 0
print(max(lst_max))