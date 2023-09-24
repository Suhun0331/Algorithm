lst = list(input())

alpha = [0]*26

for i in lst:
    alpha[ord(i)-ord('a')] += 1

for i in alpha:
    print(i, end = ' ')