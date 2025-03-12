'''
누적합.
벌집이 맨 왼쪽 / 맨 오른쪽 / 가운데
맨 왼쪽 -> 벌 하나는 무조건 맨 오른쪽,
36 + 1 ~ 마지막 한 번씩 돌면서 누적합[i-1] + 36-arr[i] 의 최댓값
맨 오른쪽도 마찬가지
가운데 : (누적합[i]-누적합[0]) + (누적합[-1] - 누적합[i])의 최댓값 
'''

n = int(input())
arr = list(map(int, input().split()))
answer = 0

sum_arr = [0] * len(arr)
sum_arr[0] = arr[0]
for i in range(1, len(arr)):
    sum_arr[i] = sum_arr[i-1] + arr[i]

for i in range(1, len(arr)-1):
    # 벌집이 맨 왼쪽
    answer = max(answer, sum_arr[i-1] + sum_arr[-2] - arr[i])
    #print(i, 'one', answer) # 1 101 102 103 104
        
    #벌집이 맨 오른쪽
    answer = max(answer, sum_arr[-1] - arr[0] + sum_arr[-1]-sum_arr[i]-arr[i])
    #print(i, 'two', answer)
    #벌집이 가운데
    answer = max(answer, sum_arr[i]-sum_arr[0] + sum_arr[-2]-sum_arr[i-1])
    #print(i, 'three', answer) # 2 7 11 (7 - 2 + 11 - 7)
    
    #print(answer)

print(answer)
# 1 100 1 1 100 1 -> 204

