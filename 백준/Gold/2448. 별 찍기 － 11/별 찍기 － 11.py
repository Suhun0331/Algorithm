

def draw_star(n):
    if n == 3:
        return ['  *  ',
                ' * * ',
                '*****']
    star = draw_star(n//2)
    result = []
    for i in star:
        result.append(' '*(n//2) + i + ' '*(n//2))
    for i in star:
        result.append(i + ' ' + i)

    return result    


    
ans = draw_star(int(input()))
for a in ans:
    print(a)
