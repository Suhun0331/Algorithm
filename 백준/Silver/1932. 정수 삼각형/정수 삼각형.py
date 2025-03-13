'''
삼각형이랑 크기 똑같은 이차원 배열 만들어서
누적합 구하면 되는 거 아닌가?
'''
n = int(input())

arr = []
sumarr = [[0] * i for i in range(1, n+1)]
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):# 층
    for j in range(len(arr[i])):# 왼쪽에서 몇 번째
        if i == 0:
            sumarr[0][0] = arr[0][0]
            break
        if j == 0: # 맨 왼쪽
            sumarr[i][j] = arr[i][j] + sumarr[i-1][j]
        elif j == len(arr[i])-1: # 맨 오른쪽
            sumarr[i][j] = arr[i][j] + sumarr[i-1][j-1]
        else:
            sumarr[i][j] = arr[i][j] + max(sumarr[i-1][j], sumarr[i-1][j-1])
#print(sumarr)
print(max(sumarr[-1]))
