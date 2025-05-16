'''
마지막에 이동거리가 1이어야 하므로 가까워질수록 줄어야 함
처음에 1 -> 2 -> 3 -> . . .-> 10 -> . . . 3 -> 2 -> 1 형태로 가야함
이런 식으로 피크는 한 번, 나머지는 두 번씩 거리가 더해짐.
피크 한 번 해서 거리를 구했을 때 목표 지점을 넘어가버리면 피크 줄여야 함
ex) 피크가 6인데 목표를 넘음 -> 피크 5로 바꿈 -> 부족 -> (부족한수//피크) 더해주고, + 1
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    len = y-x
    pick = 0
    sum = 0
    answer = 0
    while True:
        # print('pick : ', pick, 'sum : ', sum)
        if sum + pick + pick + 1 < len:
            # print('check1')
            sum = sum + pick + pick + 1
            answer += 1
            pick += 1
            continue
        elif sum + pick + pick + 1 == len:
            # print('check2')
            pick += 1
            print(pick*2-1)
            break
        else:
            # print('check3')
            answer = pick*2-1
            pickcount = ((len-sum)//pick)
            answer += pickcount
            sum += pickcount*pick
            if sum == len:
                print(answer)
            else:
                print(answer+1)
            break
        # print()