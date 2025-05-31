n, m = map(int, input().split())
square = [list(map(int, input())) for _ in range(n)]

size = min(n, m)

def find_square(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
        
            if square[i][j] == square[i][j+s-1] == square[i+s-1][j] == square[i+s-1][j+s-1]:
                return True
            
    return False
    
for k in range(size, 0, -1):
    if find_square(k):
        print(k ** 2)
        break