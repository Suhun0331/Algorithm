import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
team1 = []
team2 = []
visited = [False] * (n+1)
diff = 100

def calc(team1, team2):
    global diff
    score1 = 0
    score2 = 0
    for i in range(len(team1)):
        for j in range(i, len(team1)):
            if i == j:
                continue
            score1 += arr[team1[i]][team1[j]]
            score1 += arr[team1[j]][team1[i]]
    
    for i in range(len(team2)):
        for j in range(i, len(team2)):
            if i == j:
                continue
            score2 += arr[team2[i]][team2[j]]
            score2 += arr[team2[j]][team2[i]]
    diff = min(diff, abs(score1 - score2))
    


def dfs(start):
    global team2
    if len(team1) == n//2:
        for i in range(n):
            if i not in team1:
                team2.append(i)
        calc(team1, team2)
        return
    for i in range(start,n):
        if visited[i]:
            continue
        visited[i] = True
        team1.append(i)
        dfs(i)
        visited[i] = False
        team1.pop()
        team2 = []
        
dfs(0)
print(diff)


