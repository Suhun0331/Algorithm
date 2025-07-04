t = int(input())
for _ in range(t):
    n = int(input())
    p = [0] * (101)

    p[0], p[1], p[2], p[3], p[4] = 1, 1, 1, 2, 2

    for i in range(5, n):
        p[i] = p[i-1] + p[i-5]
    #print(p)
    print(p[n-1])