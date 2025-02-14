'''
itertools 중에 product라는 애 사용하면 될듯

이거 되면 dfs로도 풀어봐야지
'''
from itertools import product

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    arr = []
    final = []
    for i in range(1, 6):
        arr.extend(list(product(alpha, repeat = i)))
        
    for i in arr:
        final.append(''.join(map(str, i)))
    final.sort()
    #print(final[:10])
    
    return final.index(word)+1
        
        
        
        