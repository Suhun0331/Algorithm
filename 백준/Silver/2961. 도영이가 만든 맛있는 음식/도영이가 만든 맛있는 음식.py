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

arr = [[] for _ in range(n+1)]
arr[0].append((1, 0))
'''
for i in range(1, len(source)+1): # 1 ~ 2
    for pre_source in source: # 3,8 / 5,8
        for pre_s, pre_b in arr[i-1]:
            arr[i].append((pre_s*pre_source[0], pre_b+pre_source[1]))
'''
prev = [(1, 0)]
for s, b in source:
    new = prev[:]
    for ps, pb in prev:
        new.append((ps * s, pb + b))
    prev = new 
    
arr = arr[n]
answer = 1000000000
del prev[0]
#print(prev)
for i in prev:
    if abs(i[0] - i[1]) < answer:
        answer = abs(i[0] - i[1])
print(answer)
    
