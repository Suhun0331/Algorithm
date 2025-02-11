'''
[[], [], [] . . . 10개]
앞 재료부터 시작해서 얘를 썼을때 / 안썼을때 신맛, 쓴맛을 각 저장
마지막 행에서 두 값을 뺀 절댓값 가장 작은거 출력
'''
n = int(input())

source = []
for i in range(n):
    s, b = map(int, input().split())
    source.append([s, b])

prev = [(1, 0)]
for s, b in source:
    new = prev[:]
    for ps, pb in prev:
        new.append((ps * s, pb + b))
    prev = new 
    
answer = 1000000000
del prev[0]

for i in prev:
    if abs(i[0] - i[1]) < answer:
        answer = abs(i[0] - i[1])
print(answer)
    
