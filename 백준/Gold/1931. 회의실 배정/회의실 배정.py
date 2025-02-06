from sys import stdin

N = int(stdin.readline())
conf = []
for i in range(N):
    s, e = map(int, stdin.readline().split())
    conf.append((s, e))
conf.sort(key=lambda x: (x[0], x[1]))

total = 0
last_start = 0
last_end = 0
for start, end in conf:
    if last_end<=start:
        total+=1
        last_start, last_end = start, end
    elif last_end>end :
        last_start, last_end = start, end
        
print(total)