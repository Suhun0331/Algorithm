import sys
n = int(sys.stdin.readline())

lst = [list(map(int,list(sys.stdin.readline().strip()))) for i in range(n)]
answer = []
def cut(x, y, n):
    color = lst[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != lst[i][j]:
                answer.append('(')
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                answer.append(')')
                return
    answer.append(color)
    

cut(0,0,n)    

for i in answer:
    print(i, end = '')
    
