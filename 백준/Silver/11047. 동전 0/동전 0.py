n, k = map(int, input().split())

arr = []
result = 0
for i in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)

while k != 0:
    for i in range(n):
        if k>=arr[i]:
            result += k//arr[i]
            k = k%arr[i]
print(result)

