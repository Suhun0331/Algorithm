a = list(input())
a.append(' ')

stack = []
check = 0
openn = False
string = ''

for i in a:
    if i == '<':
        if stack:
            while stack:
                string += stack.pop()
        openn = True
        string += '<'
    elif i != '>' and openn == True:
        string += i
    elif i == '>':
        openn = False
        string += '>'
    elif openn == False and i != ' ':
        stack.append(i)
    elif openn == False and i == ' ':
        while stack:
            string += stack.pop()
        string += ' '
print(string)