import sys

num = int(sys.stdin.readline())

ans_lst = [0]*(10001)

for i in range(num):
    a = int(sys.stdin.readline())
    ans_lst[a] += 1
    
for i in range(10001):
    for _ in range(ans_lst[i]):
        print(i)