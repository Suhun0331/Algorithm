import sys

lst = [True for i in range(1000000)]

for i in range(2, 1001):
    if lst[i]:
        for j in range(i+i, 1000000, i):
            lst[j] = False
while True:
    #prm = False
    num = int(sys.stdin.readline())
    if num == 0:
        break
    for i in range(3, len(lst), 2):
        if lst[i] and lst[num-i]:
            print("{} = {} + {}".format(num, i,num-i))
            #prm = True
            break
    #if prm == False:
        #print("Goldbach's conjecture is wrong.")