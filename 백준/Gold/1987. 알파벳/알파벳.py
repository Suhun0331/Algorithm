'''
dfs 문제
dfs 들어갈 때 해당 알파벳 visited 처리, 나올 때 visited = False처리
최대한으로 들어가서 더이상 갈 곳이 없을 때의 depth를 max_depth와 비교

알파벳 visited 처리 어떻게? -> set 쓰고 if 'A' in set() 하면 O(1)이라 함.
* set과 dict로 in 연산자는 list와 다르게 O(1) *
-> 시간초과 ..?
-> GPT의 풀이대로 check 없애고 dfs 들어올 때마다 갱신하는 방식 사용 

'''
import sys
input = sys.stdin.readline
r, c = map(int, input().split()) # r - 세로, c - 가로 -> (r, c)
alpha = []
for i in range(r):
    alpha.append(list(input().strip()))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = set()
visited.add(alpha[0][0])
count = 1
answer = 0
#print(alpha)
def dfs(r, c, count):
    global answer
    answer = max(answer, count)
    #print(count, r, c)
    check = 0
    for i in range(4):
        nr, nc = r+dx[i], c+dy[i]
        #print(visited, nr, nc)
        if 0<= nr < len(alpha) and 0 <= nc < len(alpha[0]) and alpha[nr][nc] not in visited:
            visited.add(alpha[nr][nc])
            #print(map[nr][nc])
            
            dfs(nr, nc, count+1)
            
            visited.remove(alpha[nr][nc])
            '''
        else:
            check += 1
    if check == 4: # 4방향 다 막힘        
        answer = max(answer, count)
        count -= 1
        '''

dfs(0, 0, count)
print(answer)
