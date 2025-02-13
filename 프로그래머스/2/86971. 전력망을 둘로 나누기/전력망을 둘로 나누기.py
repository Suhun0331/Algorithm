def dfs(num, arr, visited):
    visited[num] = True
    count = 1 
    for i in arr[num]:
        if not visited[i]:
            count += dfs(i, arr, visited)
    return count

def solution(n, wires):
    arr = [[] for _ in range(n+1)]
    answer = float('inf')  
    
    for a, b in wires:
        arr[a].append(b)
        arr[b].append(a)
    
    for a, b in wires:
        visited = [False] * (n + 1)
        
        arr[a].remove(b)
        arr[b].remove(a)

        cnt1 = dfs(a, arr, visited)
        cnt2 = n - cnt1
        answer = min(answer, abs(cnt1 - cnt2))

        arr[a].append(b)
        arr[b].append(a)
        
    return answer
