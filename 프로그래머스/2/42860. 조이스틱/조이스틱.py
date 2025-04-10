'''
어차피 a가 아니라면 이동해서 위/아래로 움직여야 하는건 마찬가지
a를 기준으로 목표 알파벳이 위가 가까운지 아래가 가까운지 계산 후 움직이기

a를 통과해서 움직이는 방식을 잘 생각해봐야 할 듯
이 문제의 핵심은 a가 아닌 알파벳들을 어떤 경로로 찍느냐 를 잘 생각해봐야 하는 문제인 듯?

dfs? 현재 위치 기준으로 오른쪽으로 이동 / 왼쪽으로 이동 두 경로에 따라 dfs 진행
그냥 시작할 때 name 길이에 해당하는 list 만들고, a -> 해당 알파벳 이동 횟수 저장
왼 / 오 나눠서 dfs 진행

종료 조건 -> 더이상 왼쪽 / 오른쪽 이동할 곳이 없을 때

현재 위치에서 가장 가까운 왼/오 인덱스 어떻게 찾지?
아직 맞춰지지 않은 알파벳 저장하는 리스트 만들기?
그냥 name 길이의 반 잘라서 그만큼 왼/오 이동 후 찾은 인덱스로 다시 dfs
'''
import sys
sys.setrecursionlimit(10**6)

def solution(name): # a b c d e f g h i j k l m n o p q r s t u v w x y z
    
    def dfs(current, curanswer):
        nonlocal answer
        curanswer += cntlist[current]
        visited[current] = True
        
        if all(visited):
            answer = min(answer, curanswer)
            visited[current] = False
            return
        
        left, right = current, current
        move_left = 0
        move_right = 0
        for i in range(len(name)):
            move_left += 1
            left -= 1
            if left == -1:
                left = len(name)-1
            if not visited[left]:
                break
                
        for i in range(len(name)):
            move_right += 1
            right += 1
            if right == len(name):
                right = 0
            if not visited[right]:
                break
                
        dfs(left, curanswer + move_left)
        
        dfs(right, curanswer + move_right)
        
        visited[current] = False
    
    cntlist = [0] * len(name)
    visited = [False] * len(name)
    for i in range(len(name)):
        if name[i] == 'A':
            visited[i] = True
    current = 0
    for i in range(len(name)):
        if ord(name[i]) - ord('A') <= 13:
            cntlist[i] = ord(name[i]) - ord('A')
        else:
            cntlist[i] = ord('Z') - ord(name[i]) + 1
    curanswer = 0
    answer = float('inf')
    
    dfs(0, 0)
    return answer





