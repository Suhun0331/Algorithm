import sys

num = int(sys.stdin.readline())
for i in range(num):
    a, b = map(int,sys.stdin.readline().split())
    maxx = 0
    if a>b:
        m = a
        i = b
    else:
        m = b
        i = a
    while i != 0:
         m, i = i, m%i
    
    print((a*b)//m)
