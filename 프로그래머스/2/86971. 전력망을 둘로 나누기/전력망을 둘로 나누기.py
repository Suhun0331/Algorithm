import copy

def dfs(num, arr, visited):
    visited[num] = True
    count = 1
    for i in arr[num]:
        if not visited[i]:
            count += dfs(i, arr, visited)
            
    return count
    
        
def solution(n, wires):
    arr = [[] for _ in range(n+1)]
    answer = 100
    for i in wires:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])
    for i in wires:
        visited = [False] * (n+1)
        copy_arr = copy.deepcopy(arr)
        copy_arr[i[0]].remove(i[1])
        copy_arr[i[1]].remove(i[0])
        
        cnt1 = dfs(i[0], copy_arr, visited)
        cnt2 = dfs(i[1], copy_arr, visited)
        
        answer = min(answer, abs(cnt1 - cnt2))
        
    return answer
        
        
