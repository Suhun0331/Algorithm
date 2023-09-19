a, b = map(int, input().split())

n_list = list(map(int, input().split()))
result = []
for i in n_list:
    if(i < b):
        print(i,end=" ")
