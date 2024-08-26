#처음에 아이디어 잘 안떠오름
#[1] 인덱스 기준으로 정렬하는 법 몰랐음 

import sys
input = sys.stdin.readline

n = int(input())

arr = []
result = 1
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: (x[1], x[0]))
current = arr[0]

for i in range(n-1):
    if current[1] <= arr[i+1][0]:
        current = arr[i+1]
        result += 1

print(result)
