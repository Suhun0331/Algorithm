'''
검색한 풀이
'''

def solution(citations):
    
    citations.sort(reverse = True) # 6 5 2 1 0 -> 2
    
    for i in range(len(citations)):
        if i+1 > citations[i]:
            return i
        
    return len(citations)