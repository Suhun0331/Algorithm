n, m = map(int,input().split())

def two_div(n):
    cnt = 0
    while n>=2:
        cnt += n//2
        n = n//2
    return cnt

def five_div(n):
    cnt = 0
    while n>=5:
        cnt += n//5
        n = n//5
    return cnt

two = two_div(n)-two_div(m)-two_div(n-m)
five = five_div(n)-five_div(m)-five_div(n-m)
print(min(two,five))