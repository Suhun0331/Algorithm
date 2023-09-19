N, M = map(int,input().split())

n_list=[]
for i in range(N):
    n_list.append(i+1)

for i in range(M):
    a, b = map(int,input().split())
    n_list[a-1],n_list[b-1] = n_list[b-1],n_list[a-1]

for i in n_list:
    print(i,end=" ")
    