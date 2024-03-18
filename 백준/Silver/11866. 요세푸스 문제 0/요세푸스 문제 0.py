import sys

k, n = map(int, sys.stdin.readline().split())

lst = [i for i in range(1,k+1)]
ans = []
cnt = 0
for _ in range(len(lst)):
    cnt += (n-1)
    while(cnt >= len(lst)):
        cnt -= len(lst)
    ans.append(lst[cnt])
    del lst[cnt]
result = '<' + ', '.join([str(i) for i in ans]) + '>'
print(result)

