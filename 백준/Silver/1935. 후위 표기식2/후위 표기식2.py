num = int(input())

word = list(input())
numlst = []
for i in range(num):
    numlst.append(int(input()))

numstack = []
num1 = 0
num2 = 0
for i in word:
    if i.isalpha():
        numstack.append(numlst[ord(i)-ord('A')])
        #print(numstack)
    else:
        num1 = numstack.pop()
        num2 = numstack.pop()
        if i == '+':
            numstack.append(num2+num1)
        elif i == '-':
            numstack.append(num2-num1)
        elif i == '*':
            numstack.append(num2*num1)
        elif i == '/':
            numstack.append(num2/num1)
print("%.2f"%(numstack[0]))