n = int(input())

move = list(map(int,input().split()))

lst = [i for i in range(n)]

ans = []
cnt = 0
for _ in range(n):
    ans.append(lst[cnt])
    del lst[cnt]
    if not lst:
        break
    if move[ans[-1]] > 0:
        cnt += move[ans[-1]] -1
    else:
        cnt += move[ans[-1]]
    while cnt < 0 or cnt >=len(lst):
        if cnt < 0:
            cnt += len(lst)
        else:
            cnt %= len(lst)
for i in ans:
    print(i+1, end = ' ')
