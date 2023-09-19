x_lst = []
y_lst = []

for i in range(3):
    a, b = map(int,input().split())
    x_lst.append(a)
    y_lst.append(b)

x_ans = 0
y_ans = 0
for i in range(3):
    if x_lst.count(x_lst[i]) == 1:
        x_ans = x_lst[i]
    if y_lst.count(y_lst[i]) == 1:
        y_ans = y_lst[i]
print(x_ans,y_ans)