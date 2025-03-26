'''
예전에 비슷한 문제 풀었던 거 같은데 ... -> 두 용액
일단 오름차순 정렬

처음에 두 용액 푸는 방법 까먹고 left, right 구해서 그거 mid 처리하는 방식 썼음
그랬더니 반복문 종료조건 처리하기 너무 힘들어서 계속 무한반복

두 용액처럼 left right 양 끝에서 시작해서 하나씩 가운데로 모으는데
이건 세 용액이니까 숫자 하나 고정하고 나머지 두 숫자 처리하는 방식 쓰면 됨
gpt한테 힌트 얻어서 다시 풂
-> 시간초과 ㅋ.ㅋ ..


'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
hap = float('inf')
answerlist = [0, 0, 0]
for i in range(n-2):
    left = i+1
    right = n-1
    while left < right:
        answer = arr[i] + arr[left] + arr[right]
        if abs(hap) > abs(answer):
            hap = answer
            answerlist = [arr[i], arr[left], arr[right]]
            
        if answer > 0:
            right -= 1
        elif answer < 0:
            left += 1
        else:
            print(arr[i], arr[left], arr[right])
            sys.exit()

for i in answerlist:
    print(i, end = ' ')


    
