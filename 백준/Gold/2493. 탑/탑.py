'''
값들이 커서 완탐은 x
왼쪽부터 vs 오른쪽부터
if 왼쪽부터 -> 지금까지 중 가장 높은 탑 저장
만약 현재 탑이 가장 높은 탑보다 높으면, 0이고, 가장 높은 탑 업데이트
만약 바로 앞 탑보다 높으면, 바로 앞 탑이 닿은 탑을 확인.
그 탑보다도 높으면, 또 그 탑이 닿은 탑을 확인
-> 완탐이 아니라 점프 하면서 가능

-----------------------
스택 사용 -> (값, 인덱스) 저장해서 앞의 값들보다 큰 값 들어오면
현재 값보다 작은 애들 다 삭제 (어차피 가려지니까 이제 필요 없음)
'''
import sys
input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().split()))
stack = [(numlist[0], 0)]
print(0, end = ' ')

for i in range(1, n):
    while True:
        if not stack:
            stack.append((numlist[i], i))
            print(0, end = ' ')
            break
        
        if stack[-1][0] <= numlist[i]:
            stack.pop()
        else:
            print(stack[-1][1] + 1, end =' ')
            stack.append((numlist[i], i))
            break