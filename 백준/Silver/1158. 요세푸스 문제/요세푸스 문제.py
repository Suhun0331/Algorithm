a, b = map(int,input().split())

lst = []
count = 0
answer = []
bb = b-1
for i in range(1,a+1):
    lst.append(i)

for i in range(a):
    count += bb
    if count >= len(lst):
        count %= len(lst)
    answer.append(str(lst[count]))
    lst.pop(count)
    #del lst[count]
        
print("<"+", ".join(answer)+">")