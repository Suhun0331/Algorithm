from itertools import permutations

n = int(input())

arr = [i for i in range(1, n+1)]
arr = list(permutations(arr, n))

for i in arr:
    for j in i:
        print(j, end = ' ')
    print()
