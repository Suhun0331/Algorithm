a = input()
num = 0
sen = ['ABC', 'DEF', 'GHI','JKL','MNO','PQRS','TUV','WXYZ']

for i in sen:
    for j in a:
        if(j in i):
            num += sen.index(i)+3
    
print(num)