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
    while True:
        aa = m%i
        if aa == 0:
            maxx = i
            break
        if i%aa == 0:
            maxx = aa
            break
        else:
            m = i
            i = aa
    print((a*b)//maxx)