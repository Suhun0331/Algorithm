N, M = map(int,input().split())

n_list=[]
for i in range(N):
    n_list.append(0)

for i in range(M):
    a, b, c = map(int,input().split())
    for j in range(a-1,b):
        n_list[j] = c

for i in n_list:
    print(i,end=" ")