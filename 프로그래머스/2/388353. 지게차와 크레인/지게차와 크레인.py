'''
일단 받아온 값 2차원 배열로 저장
알파벳 1개일 때 / 2개일 때
1개일 때 -> 빈 곳이 있는 애들을 따로 리스트에 모아서 저장해놓으면 될 듯
그리고 1개 입력 받을 때 해당 리스트에 있는 애들 삭제?
좌표도 같이 저장해서 삭제된 애들의 상하좌우에 있는 애들이 리스트 안에 없으면 추가
2개일 때 -> 그냥 2차원 배열 돌면서 찾으면 삭제, 삭제할 때 상하좌우에 있는 애들 리스트 안에 없으면 추가
'''
def solution(storage, requests):
    answer = 0
    arr = [list(i) for i in storage]
    empty = []
    visited = set()
    
    def check(n, m):
        if (n, m) in visited:
            return
        visited.add((n,m))
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            xx,yy = m + dx[i], n + dy[i]
            if 0 <= yy < len(storage) and 0 <= xx < len(storage[0]):
                if arr[yy][xx] == '0':
                    check(yy, xx)
                elif (arr[yy][xx], yy, xx) not in empty :
                    empty.append((arr[yy][xx], yy, xx))
                
                    
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if i==0 or j==0 or i == len(storage)-1 or j == len(storage[0])-1:
                empty.append((storage[i][j], i, j))
                
    for i in requests:
        to_remove = []
        if len(i) == 1:
            for (value, n, m) in empty[:]:
                if i == value:
                    to_remove.append((i, n, m))
                    
        else:
            for j in range(len(storage)):
                for k in range(len(storage[0])):
                    if arr[j][k] == i[0]:
                        to_remove.append((i[0], j, k))
                        
        for v, n, m in to_remove:
            if (v, n, m) in empty:
                check(n, m)
            arr[n][m] = '0'
        empty = [item for item in empty if item not in to_remove]
        
    return sum(j != '0' for i in arr for j in i)
    