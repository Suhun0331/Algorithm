lst = list(input())
num = ''
number = []
oper = []
for i in lst:
    if i != '+' and i != '-':
        num += i
    else:
        oper.append(i)
        number.append(int(num))
        num = ''
number.append(int(num))

minus = False
answer = 0
answer += number[0]
for i in range(1, len(number)): # 1 2
    if oper[i-1] == '-':
        minus = True
        answer -= number[i]
    elif oper[i-1] == '+' and minus == True:
        answer -= number[i]
    else:
        answer += number[i]

print(answer)
