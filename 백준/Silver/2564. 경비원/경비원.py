def get_dist(p, dist):
    if p == 1:
        return dist 
    elif p == 2:
        return m + n + m - dist 
    elif p == 3:
        return m + n + m + n - dist 
    else:
        return m + dist 

m, n = map(int,input().split())

x = int(input())

pos = []
for i in range(x + 1):
    if i == x:
        d_pos, d_dist = map(int,input().split())
    else:
        pos.append(list(map(int, input().split()))) 

sum_value = 0
path1 = get_dist(d_pos, d_dist)
for p, dist in pos:
    path2 = get_dist(p, dist)

    dist1 = abs(path1 - path2)
    dist2 = 2*m + 2*n - dist1

    sum_value += dist1 if dist1 < dist2 else dist2 
    
print(sum_value)