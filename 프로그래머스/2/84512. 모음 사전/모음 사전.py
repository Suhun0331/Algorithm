def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    count = 0
    answer = 0
    find = False
    def dfs(sentence):
        nonlocal answer, find, count
        if find:
            return
        if sentence == word:
            answer = count
            find = True
            return
        count += 1
        if len(sentence) == 5:
            return
        for i in range(5):
            dfs(sentence+alpha[i])
    dfs('')
    return answer