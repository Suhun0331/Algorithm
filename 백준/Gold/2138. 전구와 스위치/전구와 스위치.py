n = int(input())

current = list(map(int, input()))
want = list(map(int, input()))

def change(a,b):
    a_copy = a[:]
    count = 0
    for i in range(1, n):
        if a_copy[i-1] == b[i-1]:
            continue

        a_copy[i-1] = 1-a_copy[i-1]
        a_copy[i] = 1-a_copy[i]
        if i<n-1:
            a_copy[i+1] = 1-a_copy[i+1]
        count += 1


    if a_copy == b:
        return count
    else:
        return 1e9
    

res = change(current, want)

current[0] = 1-current[0]
current[1] = 1- current[1]


res = min(res, change(current, want)+1)

if res == 1e9:
    print(-1)
else:
    print(res)

            
