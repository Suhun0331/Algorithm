n = input().split('-')

temp = []
for i in n:
    num = i.split('+')
    summ = 0
    for j in num:
        summ += int(j)
    temp.append(summ)

answer = 0
answer += temp[0]
for i in temp[1:]:
    answer -= i

print(answer)
