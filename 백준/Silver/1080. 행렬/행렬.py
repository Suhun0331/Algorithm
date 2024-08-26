#ㄹㅇ 아이디어 1도 안떠오름

a, b = map(int, input().split())

arr1 = []
arr2 = []
result = 0

for i in range(a):
    arr1.append(list(map(int, input())))

for i in range(a):
    arr2.append(list(map(int, input())))

for i in range(1, a-1):
    for j in range(1, b-1):
        if arr1[i-1][j-1] != arr2[i-1][j-1]:
            result += 1
            for k in range(3):
                for q in range(3):
                    arr1[i-1+k][j-1+q] = 1-arr1[i-1+k][j-1+q]

if arr1 != arr2:
    print(-1)
else:
    print(result)
        
