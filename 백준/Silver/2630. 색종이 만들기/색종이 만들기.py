import sys
n = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
blue = 0
white = 0
def cut(x, y, n):
    global blue
    global white
    color = lst[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != lst[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if color == 1:
        blue += 1
    else:
        white += 1

cut(0,0,n)
print(white)
print(blue)