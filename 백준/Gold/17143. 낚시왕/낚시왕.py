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
'''
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
shark = []
answer = 0
weight = 0
for i in range(M):
    shark.append(list(map(int, input().split())))

def move(r, c, s, d, z):
    if d == 1 or d == 2: # 위/아래 - r 변경
        s %= 2 * (R-1) # 사이클 나눠서 이동 최소화
        for _ in range(s):
            if r == 1:
                d = 2
            elif r == R:
                d = 1
                
            if d == 1:
                r -= 1
            elif d == 2:
                r += 1
                
    elif d == 3 or d == 4: # 오른쪽/왼쪽 - c 변경
        s %= 2 * (C-1)
        for _ in range(s):
            if c == 1:
                d = 3
            elif c == C:
                d = 4
                
            if d == 3:
                c += 1
            elif d == 4:
                c -= 1
    return r, c, d

for i in range(1, C+1): # 1초부터 C초까지
    next_shark = {}
    # highshark = [101, 101]

    min_row = R + 1
    target_idx = -1
    for idx, (r, c, s, d, z) in enumerate(shark):
        if c == i and r < min_row:
            min_row = r
            target_idx = idx
    
    if target_idx != -1:
        answer += shark[target_idx][4]
        shark.pop(target_idx)
    
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
