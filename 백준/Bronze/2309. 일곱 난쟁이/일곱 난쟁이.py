import sys
input = sys.stdin.readline

num = []

for _ in range(9):
    num.append(int(input()))

for i in range(8): # 0 ~ 7
    for j in range(i, 9): # i ~ 8
        copy = num[:]
        del copy[j]
        del copy[i]
        if sum(copy) == 100:
            copy.sort()
            for n in copy:
                print(n)
            exit()