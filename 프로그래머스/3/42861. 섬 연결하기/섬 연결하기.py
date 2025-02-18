'''
크루스칼 알고리즘(유니온 파인드)
'''



def solution(n, costs):
    
    def find_parent(parent, n):
        if parent[n] != n:
            parent[n] = find_parent(parent, parent[n])
        return parent[n]

    def union_parent(parent, n1, n2):
        a = find_parent(parent, n1)
        b = find_parent(parent, n2)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    
    parent = [i for i in range(n+1)]
    costs.sort(key = lambda x : x[2])
    answer = 0
    
    for i in costs:
        n1, n2, cost = i
        if find_parent(parent, n1) != find_parent(parent, n2):
            answer += cost
            union_parent(parent, n1, n2)
        
    return answer