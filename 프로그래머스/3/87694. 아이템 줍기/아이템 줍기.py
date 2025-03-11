'''
2차원 배열 만들어서 테두리만 표시? / 전체 다 표시 후 테두리만 따라가기?
테두리만 표시하는게 효율적일 듯.
사각형 입력 받으면 각 사각형 전체 다 1로 표시한 후에
전체 반복문 돌면서 테두리만 남기기(1인 칸 중 상하좌우 모두 1이면 테두리 x)
그 후 두 방향 중 더 가까운 방향 선택.
'''
import copy

def solution(rectangle, characterX, characterY, itemX, itemY):
    global answer
    answer = float('inf')
    cnt = 0
    arr = [[0]*(52*2) for _ in range(52*2)]
    
    for i in rectangle:
        x1, y1, x2, y2 = i[0]*2, i[1]*2, i[2]*2, i[3]*2
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if arr[x][y] != 1:
                    arr[x][y] = 1
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]

    copy_arr = copy.deepcopy(arr)
    for i in range(1, 52*2):
        for j in range(1, 52*2):
            if copy_arr[i][j] == 1:
                side = False
                for k in range(8):
                    xx, yy = i + dx[k], j + dy[k]
                    if 0<= xx < 52*2 and 0 <= yy < 52*2:
                        if copy_arr[xx][yy] == 0:
                            side = True
                            break
                if not side:
                    arr[i][j] = 0
                
    visited = [[False]*52*2 for _ in range(52*2)]
    
    count = 0
    def dfs(x, y, count):
        global answer
        if arr[x][y] == 0 or visited[x][y]:
            return
        if (x, y) == (itemX*2, itemY*2):
            answer = min(answer, count)
            return
        
        visited[x][y] = True
        
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0<= xx < 52*2 and 0 <= yy < 52*2:
                dfs(xx, yy, count+1)
            # visited[xx][yy] = False
            
            
    dfs(characterX*2, characterY*2, count)
    
    return answer//2