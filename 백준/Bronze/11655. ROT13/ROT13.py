lst = list(input())
answer = []

for i in lst:
    if i.islower():
        i = chr(ord(i)+13)
        if ord(i)<=ord('z'):
            answer.append(i)
        else:
            i = chr(ord(i)-26)
            answer.append(i)
    elif i.isupper():
        i = chr(ord(i)+13)
        if ord(i)<=ord('Z'):
            answer.append(i)
        else:
            i = chr(ord(i)-26)
            answer.append(i)
    else:
        answer.append(i)

for i in answer:
    print(i, end = '')