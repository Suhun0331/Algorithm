num = int(input())
mul = 1
for i in range(1, num+1):
    mul *= i

div = 10
summ = 0
while True:
    if mul%div == 0 and mul>= div:
        summ += 1
        div *= 10
    else:
        break
print(summ)