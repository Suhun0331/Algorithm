import sys

num = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
set_lst = list(set(lst))
set_lst.sort()

dic = {}
for i in range(len(set_lst)):
    dic[set_lst[i]] = i
     
for i in lst:
    print(dic[i], end = ' ')