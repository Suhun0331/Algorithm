'''
gifts 탐색 하면서 주고받은 기록 저장
그 후 이중for문 사용해서 친구들 사이 관계 탐색?
a b c d -> a - bcd , b - cd, c - d식으로 탐색

a와 b 탐색할 때 서로 주고받은 수 확인 -> 같으면 선물 지수 탐색
딕셔너리 사용해서 사람 이름 번호 매기기

받은 리스트, 준 리스트 만들기
give[a][b] = 3 -> a가 b에게 3개를 줬다.
receive[b][a] = 1 -> b가 a에게 1개를 받았다.
'''
def solution(friends, gifts):
    dict = {}
    give = [[0]*len(friends) for _ in range(len(friends))]
    receive = [[0]*len(friends) for _ in range(len(friends))]
    giftscore = [0] * len(friends)
    anslist = [0] * len(friends)
    for i in range(len(friends)):
        dict[friends[i]] = i
    
    for i in gifts:
        aname, bname = i.split()
        aind, bind = dict[aname], dict[bname]

        give[aind][bind] += 1
        receive[bind][aind] += 1
    
    for i in range(len(friends)):
        giftscore[i] = sum(give[i]) - sum(receive[i])
        
    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            if give[i][j] > receive[i][j]: # i가 j한테 준게 더 많으면
                anslist[i] += 1
            elif give[i][j] < receive[i][j]: # 반대라면
                anslist[j] += 1
            else: # 같다면
                if giftscore[i] > giftscore[j]:
                    anslist[i] += 1
                elif giftscore[i] < giftscore[j]:
                    anslist[j] += 1
    return max(anslist)
                
        