n = int(input())
count = 0

for i in range(1, n+1):
    if i < 10:
        count += 1
        continue
    rule = True
    i = str(i)
    for j in range(len(i)-1): # 3자리수면 0, 1
        if j == 0:
            diff = int(i[j+1])-int(i[j])
            continue
        if int(i[j+1])-int(i[j]) != diff:
            rule = False
            break
    if rule:
        count += 1
print(count)