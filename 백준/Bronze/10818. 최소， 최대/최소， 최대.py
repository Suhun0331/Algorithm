a = int(input())

n_list = list(map(int, input().split()))
maxx = n_list[0]
minn = n_list[0]
for i in range(a-1):
    maxx = max(maxx, n_list[i+1])
    minn = min(minn, n_list[i+1])
print(minn, maxx)