a, b, c, d, e, f = map(int,input().split())
xx = 0
yy = 0
for x in range(-999,1000):
    for y in range(-999,1000):
        if(a*x + b*y == c and d*x + e*y == f):
            xx = x
            yy = y

print(xx, yy)