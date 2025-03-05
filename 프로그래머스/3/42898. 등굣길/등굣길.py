def solution(m, n, puddles):
    map = [[0]*(m+1) for _ in range(n+1)]
    for i in puddles:
        x, y = i
        map[y][x] = -1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                map[j][i] = 1
                continue
            if map[i][j] == -1:
                map[i][j] = 0
                continue
            else:
                map[i][j] = (map[i-1][j] + map[i][j-1])%1000000007
    return map[n][m] 