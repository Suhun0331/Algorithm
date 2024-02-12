num = int(input())
lst = []
for i in range(num):
    score = 0
    lst = list(input())
    cnt = 1
    for i in lst:
        if i == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)

            
