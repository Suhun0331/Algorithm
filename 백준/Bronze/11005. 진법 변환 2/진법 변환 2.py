a, b = map(int,input().split())
lst = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ''

while a!= 0:
    ans += str(lst[a%b])
    a = a//b

print(ans[::-1])