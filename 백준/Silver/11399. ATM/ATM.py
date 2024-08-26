n = int(input())


arr = list(map(int, input().split()))


arr.sort()

result = 0

for i in range(n):
    result += (i+1) * arr[n-i-1]
print(result)
