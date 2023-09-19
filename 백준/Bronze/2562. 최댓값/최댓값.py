listt=[]
for i in range(9):
    a = int(input())
    listt.append(a)

maxx = max(listt)
print(maxx)
print(listt.index(maxx)+1)