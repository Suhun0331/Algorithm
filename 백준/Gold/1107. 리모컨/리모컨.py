'''
dfs / bfs / dp
어차피 처음에 숫자를 누르고 나서는 + or -만으로 조작해야함.
처음에 제일 가까운 숫자가 뭐가 있는지 찾고, ord(목표 수 - 누른 수) 하면 됨 
근데 왜 제한시간이 2초지 ...?

목표 숫자 앞에서부터 in으로 사용 가능한 숫자인지 확인
그 숫자가 없으면 윗 숫자? 아래 숫자? 어떻게 판단하지?

조합으로 사용 가능한 숫자들 써서 ord(목표 수 - 누른 수) 제일 작은거 찾기.
근데 그러면 자릿수가 안맞는 경우를 못찾음

백트래킹으로 숫자를 점점 올리기 ..?
----------------------
완탐이었다.
-> 작은 수부터 모든 경우 다 거치다가 결과값이 더 커지면 stop
'''
from itertools import product
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m != 0:
    lst = list(map(int, input().split()))
    use = [str(i) for i in range(10) if i not in lst]
else:
    use = [str(i) for i in range(10)]
num = []
answer = float('inf')


for length in range(1, 7):
    for comb in product(use, repeat=length):
        num = int(''.join(comb))  # 만들어진 숫자
        #print(num, answer)
        if answer > abs(n-num)+len(str(num)):
            answer = abs(n-num)+len(str(num))
'''
        else:
            if abs(100-n) < answer:
                print(abs(100-n))
            else:
                print(answer)
            exit()
'''
if abs(100-n) < answer:
    print(abs(100-n))
else:
    print(answer)
