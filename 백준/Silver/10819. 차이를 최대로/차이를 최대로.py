from itertools import permutations

num = int(input())

lst = list(map(int, input().split()))

perm = permutations(lst,num)
ans = -800
for i in perm:
    s = 0
    for j in range(len(lst)-1):
        s += abs(i[j]-i[j+1])
    if ans < s:
        ans = s
print(ans)
