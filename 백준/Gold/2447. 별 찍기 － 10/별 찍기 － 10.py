def draw_star(n):
    if n == 1:
        return ['*']
    star = draw_star(n//3)
    result = []
    for i in star:
        result.append(i*3)
    for i in star:
        result.append(i + ' '*(n//3) + i)
    for i in star:
        result.append(i*3)

    return result    


    
ans = draw_star(int(input()))
for a in ans:
    print(a)
