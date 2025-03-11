'''
이분탐색? dp?
어차피 꿀통까지 움직이니까 꿀통의 위치는 상관 없을 거 같고
벌의 위치가 중요할 듯?
전체 합에서 벌 위치 빼면 될 거 같음(조합)

꿀통은 맨 오른쪽 / 맨 왼쪽 / 중간
'''
from itertools import combinations

n= int(input())
lst = list(map(int, input().split()))
arr = list(i for i in range(n))
comb = list(combinations(arr, 2))
answer = 0

for i in comb:
    left, right = i
    # 벌집이 맨 오른쪽
    answer = max(answer, sum(lst[left:]) + sum(lst[right:]) - lst[left] - lst[right] * 2)
    # 벌집이 맨 왼쪽
    answer = max(answer, sum(lst[:left+1]) + sum(lst[:right]) - lst[left] * 2)
    # 벌집이 가운데
    answer = max(answer, sum(lst[left:right+1]) + max(lst[left:right]) - lst[left] - lst[right])

print(answer)
