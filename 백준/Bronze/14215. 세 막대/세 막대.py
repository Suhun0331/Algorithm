lst = sorted(list(map(int,input().split())))

if lst[0]+lst[1] > lst[2]:
    print(sum(lst))
else:
    print((lst[0]+lst[1])*2 -1)