import copy

def solution(rectangle, characterX, characterY, itemX, itemY):
    global answer
    answer = float('inf')  # 최솟값을 찾기 위해 무한대로 초기화
    N = 52 * 2  # 2배 확장한 좌표 크기

    # 1. 2D 배열을 만들어 사각형 내부를 1로 채우기
    arr = [[0] * N for _ in range(N)]
    
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                arr[x][y] = 1

    # 2. 테두리만 남기기 (8방향 탐색)
    dx = [1, 0, -1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]

    copy_arr = copy.deepcopy(arr)
    for i in range(1, N):
        for j in range(1, N):
            if copy_arr[i][j] == 1:
                is_inner = True  # 기본적으로 내부라고 가정
                for k in range(8):  # 8방향 검사
                    xx, yy = i + dx[k], j + dy[k]
                    if 0 <= xx < N and 0 <= yy < N:
                        if copy_arr[xx][yy] == 0:  # 주변에 0이 하나라도 있으면 테두리임
                            is_inner = False
                            break
                if is_inner:
                    arr[i][j] = 0  # 내부라면 0으로 바꿔서 제거

    # 3. DFS로 최단 거리 탐색
    visited = [[False] * N for _ in range(N)]

    def dfs(x, y, count):
        global answer
        if arr[x][y] == 0 or visited[x][y]:  # 테두리가 아니거나 이미 방문한 경우
            return
        if (x, y) == (itemX * 2, itemY * 2):  # 목표 지점 도착
            answer = min(answer, count)
            return

        visited[x][y] = True
        for i in range(4):  # 상하좌우 탐색
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < N and 0 <= yy < N and not visited[xx][yy] and arr[xx][yy] == 1:
                dfs(xx, yy, count + 1)
        visited[x][y] = False  # 백트래킹

    dfs(characterX * 2, characterY * 2, 0)

    return answer // 2  # 2배 확장했으므로 결과값도 2로 나눠서 반환
