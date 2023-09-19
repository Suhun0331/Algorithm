import sys
input = sys.stdin.readline

a = int(input())

for i in range(a):
    b, c = map(int, input().split())
    print("Case #{}: {}".format(i+1, b+c))