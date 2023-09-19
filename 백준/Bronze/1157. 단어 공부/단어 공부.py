a = input().upper() #a b b c

lst = list(set(a)) # a b c

cnt = [] #0 0 0

for i in lst:
    cnt.append(a.count(i))

if(cnt.count(max(cnt)) > 1):
    print("?")
else:
    print(lst[cnt.index(max(cnt))])