'''
순차적으로 비교한다고 생각하면, 항상 비교하는 위치의 왼쪽 위는
더이상 바꿀 수 있는 기회가 없음.
그렇기 때문에 왼쪽 위 숫자가 같은지 다른지를 비교하여
값을 변경할지 결정해야함.
이 아이디어를 떠올리기가 어려웠음
'''

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
        
