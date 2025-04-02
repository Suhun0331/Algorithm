'''
단순 구현문제

1. 상어 움직임 2. 상어 잡아먹기 3. 땅에서 가까운 상어 찾기

입력받은 값 그대로 저장
1초마다 각 상어의 다음 위치 및 방향 계산 후 업데이트
1초마다 정렬할 것도 아닌데 같은 좌표인 거 어떻게 파악?

딕셔너리 사용.
1초마다 next_dict = {}로 초기화 해주고 기존 상어 하나씩 이동 및 업데이트 후 next_dict에 넣어줌
이 때 이미 값이 있다면 크기 비교해서 하나만 남김

땅에서 가까운 상어는 .. i초에서 상어 이동 후 열이 i+1인 상어들의 행을 저장하고,
다음 초에 행에 있는 애들 중 가장 작은 값을 가진 상어를 dict에서 삭제

---
상어 잡는 로직을 원래 i+1로 처리 했었는데, 그럼 맨 처음이 애매해져서
상어 이동 전에 먼저 잡고 이동시키는 방식으로 바꿈.
이 과정에서 매 초 sort를 해야하기 때문에 느려질까 했는데 그래봤자 100초까지라서 괜찮을 듯
+ enumerate 함수 -> 인덱스와 값을 같이 리턴해주기 때문에 shark 리스트에서 해당 인덱스 값 지우기 용이

1차 제출 -> 시간 초과 
pypy -> 통과 -> 상어 잡는 로직 다시 sort로 바꿔서 시간 비교 
---

상어가 이동하는걸 for문으로 하나씩 가는게 아니라 그냥 수학 계산으로 O(1)로 처리
-> 이래야 python3까지 통과됨.
move함수 못하겠어서 일단 인터넷꺼 가져다씀
-> 추후에 다시 시도 ..
'''
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
shark = []
answer = 0
weight = 0
for i in range(M):
    shark.append(list(map(int, input().split())))

def move(row, col, s, d, z):
    # 위
    if d == 1:
        if row - s >= 1:
            row -= s
        else:
            s -= row - 1
            direction = s // (R - 1)
            location = s % (R - 1)
            if direction % 2 == 0:
                d = 2
                row = 1 + location 
            else:
                row = R - location

    # 아래
    elif d == 2:
        if row + s <= R:
            row += s
        else:
            s -= R - row
            direction = s // (R - 1)
            location = s % (R - 1)
            if direction % 2 == 0:
                d = 1
                row = R - location 
            else:
                row = 1 + location

    # 오른쪽
    elif d == 3:
        if col + s <= C:
            col += s
        else:
            s -= C - col
            direction = s // (C - 1)
            location = s % (C - 1)
            if direction % 2 == 0:
                d = 4
                col = C - location 
            else:
                col = 1 + location

    # 왼쪽
    elif d == 4:
        if col - s >= 1:
            col -= s
        else:
            s -= col - 1
            direction = s // (C - 1)
            location = s % (C - 1)
            if direction % 2 == 0:
                d = 3
                col = 1 + location
            else:
                col = C - location 

    return row, col, d


for i in range(1, C+1): # 1초부터 C초까지
    next_shark = {}
    # highshark = [101, 101]

    shark.sort()
    for idx, s in enumerate(shark):
        if i == s[1]:
            answer += s[4]
            del shark[idx]
            break
    
    for r, c, s, d, z in shark:
        nr, nc, nd = move(r, c, s, d, z)
        if (nr, nc) not in next_shark:
            next_shark[(nr, nc)] = [nr, nc, s, nd, z]
        else:
            if next_shark[(nr,nc)][4] < z:
                next_shark[(nr, nc)] = [nr, nc, s, nd, z]
            else:
                continue
    #     if nc == i+1: # 다음 상어 미리 잡기 위해 다음 위치 상어들 모음
    #         if highshark[0] > nr:
    #             highshark[0], highshark[1] = nr, nc
    #             weight = z
    # if highshark[0] != 101:
    #     answer += weight
    #     del next_shark[(highshark[0], highshark[1])]
    shark = list(next_shark.values())

print(answer)
