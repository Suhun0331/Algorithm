'''
이동에 따라 이동한 좌표 저장하고,
상하좌우 중 가장 큰 좌표값들 바탕으로 사각형 생성
'''
t = int(input())
dxdy = [(-1, 0), (0, 1),(1, 0), (0, -1)] # 북, 동, 남, 서 

for _ in range(t):
    move = list(map(str, input().strip()))
    x, y, d = 0, 0, 0 #(y, x), d = 0, 1, 2, 3(북 동 남 서)
    path = set()
    path.add((0, 0))

    for i in move:
        if i == 'F':
            dy, dx = dxdy[d]
        elif i == 'L':
            d = (d+3) % 4
            continue
        elif i == 'R':
            d = (d+1) % 4
            continue
        elif i == 'B':
            dy, dx = dxdy[(d+2)%4]
        x += dx
        y += dy
        
        path.add((y, x))
    
    min_y, min_x, max_y, max_x = float('inf'), float('inf'),0, 0
    for i in path:
        min_y = min(min_y, i[0])
        min_x = min(min_x, i[1])
        max_y = max(max_y, i[0])
        max_x = max(max_x, i[1])
    
    
    print(abs(max_x-min_x) * abs(max_y-min_y))