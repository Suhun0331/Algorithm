'''
bfs dfs 둘 다 괜찮을 듯?
일단 dfs로.
방문한 지역 또 방문할 수도 있고
dfs로 하나씩 들어갈 때마다 사용한 티켓 지웠다가, dfs 나오면 다시 티켓 추가하기
len(티켓) == 0이면 모두 방문했다는 뜻이니까 해당 경로 answer에 append
마지막에 answer 정렬한 후 맨 앞 리스트 return

16번째줄 append 하는 조건을 수정해야 함. 티켓을 모두 사용했을 때를 구해야하니까

'''
def dfs(current, route, tickets, visited, count, answer):
    if count == len(tickets):
        answer.append(route[:])
        return
    for i in range(len(tickets)):
        if current == tickets[i][0] and not visited[i]:
            route.append(tickets[i][1])
            visited[i] = True
            count += 1
            dfs(tickets[i][1], route, tickets, visited, count, answer)
            count -= 1
            visited[i] = False
            route.pop()
            

def solution(tickets):
    visited = [False] * (len(tickets)+1)
    route = ["ICN"]
    count = 0
    answer = []
    dfs("ICN", route, tickets, visited, count, answer)
    answer.sort()
    return answer[0]