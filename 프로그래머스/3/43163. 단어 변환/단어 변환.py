'''
dfs 사용
begin이 hit이면 그 다음에 올 수 있는 단어 탐색해서 dfs 탐색, count += 1
특정 dfs 단계에서 어떤 단어를 사용했는지 어떻게 판단하지 ..?
그냥 리스트 안에 단계 다 넣어놓고 in 연산자 써서 얘가 온 적 있는 애인지 확인?
한글자 다른지 확인하는건 앞에서부터 for문 돌려서 한글자씩 비교하고, 다른 알파벳 나왔을 때
그 뒤 [n:] 다 똑같은지 확인해서 같으면 한 알파벳만 다른 단어임.

이렇게 확인 하면서 target을 찾으면 return len(answer) 하고,
한 알파벳 다른 단어가 없으면 뒤로 백
'''
answer = 100
def dfs(word, wordlist, target, words):
    global answer
    print(wordlist)
    if word == target:
        answer = min(answer, len(wordlist))
        return
    for i in words: 
        if i in wordlist: # 이미 경로 중 통과한 단어라면 패스
            continue
        else:
            for j in range(len(word)):
                if word[j] != i[j]:
                    if word[j+1:] == i[j+1:]:
                        wordlist.append(i)
                        dfs(i, wordlist, target, words)
                        wordlist.pop()
                        break
                    else:
                        break
                        

def solution(begin, target, words):
    wordlist = set()
    dfs(begin, [], target, words)
    if answer == 100:
        return 0
    return answer
    
            
    