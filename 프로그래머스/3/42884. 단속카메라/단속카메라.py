'''
시작점 기준 정렬 or 끝 기준 정렬? or 절댓값 작은 기준 정렬?

1. 시작점 기준 정렬
-20 -18 -14 -5

첫 번째 타고 올라가는데, 첫 번째 범위 중 가장 뒷부분에 카메라를 설치하는게 좋음.
그런 와중에도 두 번째 카메라보다 오버되면 안되니까
a. 첫 번째 범위 중 가장 뒤 + 두 번째 범위의 끝 이전
b. 이때 설치한 카메라의 위치가 그 뒷 범위에 속하면 continue, 아니면 다시 a부터 시작

2. 끝지점 기준 정렬
-15 -13 -5 -3
'''

def solution(routes):
    answer = 0
    routes.sort(key = lambda x : (x[1], x[0]))
    point = 30001*(-1)
    visited = [False] *(len(routes) + 1)
    for i in range(len(routes) - 1): # 0 ~ 2
        if visited[i]:
            continue
        if routes[i][0] <= point <= routes[i][1]:
            visited[i] = True
            continue
            
        if routes[i][1] < routes[i+1][0]:
            answer += 1
            visited[i] = True
            point = routes[i][1]
        elif routes[i][1] >= routes[i+1][1]:
            visited[i] = True
        elif routes[i][1] == routes[i+1][0]:
            point = routes[i][1]
            answer += 1
            visited[i], visited[i+1] = True, True
        else:
            point = max(routes[i][1] , routes[i+1][0])
            visited[i] = True
            visited[i+1] = True
            answer += 1
        
    if routes[-1][0] > point:
        answer += 1
    return answer
            
        
    
    
    