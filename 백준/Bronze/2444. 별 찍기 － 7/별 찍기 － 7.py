a = int(input())

for i in range(1, a*2):
    if(i <= a):
        print(" "*(a-i) + "*"*(2*i-1))
    else:
        print(" "*(i-a) + "*"*(2*(2*a-i)-1))