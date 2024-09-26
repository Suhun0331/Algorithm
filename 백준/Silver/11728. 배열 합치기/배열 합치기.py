import sys
input = sys.stdin.readline

a, b = map(int, input().split())

alst = list(map(int, input().split()))
blst = list(map(int, input().split()))
result = alst + blst

result.sort()
for i in result:
    print(i, end= ' ')
