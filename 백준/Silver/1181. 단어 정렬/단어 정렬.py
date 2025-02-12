n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
    
arr.sort()
arr.sort(key = len)

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        print(arr[i])
print(arr[-1])
