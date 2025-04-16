'''
처음엔 진짜 각 모양 별 check함수 만들어서 다ㅏㅏ 탐색하는 코드 짬
코드도 너무 어렵고 코드도 너무 길어지고 모든걸 다 확인해야 하니까 너무 비효율적
-> 아예 모르겠어서 인터넷 답 찾아봤음.

코드 자체는 너무 쉬운 문제. 그냥 아이디어를 생각해내느냐의 문제였음.
앞으로 이런 문제 만나면 쉽게 풀 수 있는 방법이 뭐가 있을지 먼저 떠올려야 할 듯.
'''
def solution(edges):
    indegree = [0] * (1000001)
    outdegree = [0] * (1000001)
    maxnode, create, stick, donut, eight = 0, 0, 0, 0, 0
    
    for a, b in edges:
        outdegree[a] += 1
        indegree[b] += 1
        maxnode = max(maxnode, a, b)
        
    for i in range(1, maxnode+1):
        if indegree[i] == 0 and outdegree[i] >= 2:
            create  = i
        elif indegree[i] >= 1 and outdegree[i] == 0:
            stick += 1
        elif indegree[i] >= 2 and outdegree[i] == 2:
            eight += 1
            
    donut = outdegree[create] - stick - eight
    return [create, donut, stick, eight]





