llist = []

for i in range(10):
    a = int(input())
    llist.append(a)

result = []
for i in range(10):
    num = llist[i]%42
    if(num not in result):
        result.append(num)
        
print(len(result))