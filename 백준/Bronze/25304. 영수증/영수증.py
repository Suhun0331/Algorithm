a = int(input())
b = int(input())
total = 0

for i in range(b):
    c, d = map(int, input().split())
    total += c*d
    
if(total == a):
    print("Yes")
else:
    print("No")