def solution(m, n, puddles):
    map = [[0]*(m+1) for _ in range(n+1)]
    for i in puddles:
        x, y = i
        map[y][x] = -1
    for i in range(1, m+1):
        if map[1][i] != -1:
            map[1][i] = 1
        else:
            break
    for i in range(1, n+1):
        if map[i][1] != -1:
            map[i][1] = 1
        else:
            break
        
    print(map)
    for i in range(2, n+1):
        for j in range(2, m+1):
            if map[i][j] == -1:
                continue
            if map[i-1][j] == -1 and map[i][j-1] == -1:
                map[i][j] = 0
            elif map[i-1][j] == -1:
                map[i][j] = map[i][j-1]
            elif map[i][j-1] == -1:
                map[i][j] = map[i-1][j]
            else:
                map[i][j] = map[i-1][j] + map[i][j-1]
    print(map)
            
    return map[n][m]%1000000007