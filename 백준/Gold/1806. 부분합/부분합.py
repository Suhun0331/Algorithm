'''
누적합.
앞에서부터 구하면서 최소 길이 갱신
만약 앞에까지 최소길이가 5였다면
다음 인덱스에서는 길이가 5인 것부터 확인.
근데 S보다 크다면, 하나씩 줄여가고 줄이는게 가능하면 최소 길이도 갱신
+ 누적합이 S보다 작으면 continue

근데 뭔가 시간초과 뜰 거 같다 . . .
'''

n, s = map(int, input().split())

arr = list(map(int, input().split()))

sumarr = [0]*(n+1)
start = False
answer = 0
for i in range(n):
    sumarr[i] = sumarr[i-1]+arr[i]
    if sumarr[i]>= s and not start:
        start = True
        answer = i+1
#print(start)

for i in range(start, n): # 5 ~ 9
    #print(answer)
    for j in range(answer-1, -1, -1): # 4 ~ 0
        if sumarr[i] - sumarr[i-j] >= s:
            answer -= 1
        else:
            break
if start == 0:
    print(0)
else:
    print(answer)




        
    
