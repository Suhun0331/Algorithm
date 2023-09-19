num = int(input())

count3 = 0
count5 = 0

while True:
    if(num%5 == 0):
        count5 = num//5
        num = 0
    elif num>=3:
        num -= 3
        count3 += 1
    if num == 0:
        answer = count5+count3
        break
    elif num<3:
        answer = -1
        break
print(answer)