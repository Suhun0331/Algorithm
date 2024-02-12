fac = 1

def factorial(n):
    global fac
    if n == 1:
        fac *= 1
    elif n == 0:
        fac = 1
    else:
        fac *= n
        n -= 1
        factorial(n)

n = int(input())
factorial(n)

print(fac)
