'''
dfs 풀이
'''

def solution(word):
    cnt = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(arr):
        nonlocal cnt
        cnt += 1
        if word == arr:
            return True
        if len(arr) == 5:
            return False

        for i in alpha:
            if dfs(arr+i):
                return True
            list(arr).pop()
        
    for i in alpha:
        if dfs(i):
            return cnt
    
        
        
        
        