'''
gifts 탐색 하면서 주고받은 기록 저장
그 후 이중for문 사용해서 친구들 사이 관계 탐색?
a b c d -> a - bcd , b - cd, c - d식으로 탐색

a와 b 탐색할 때 서로 주고받은 수 확인 -> 같으면 선물 지수 탐색
딕셔너리 사용해서 사람 이름 번호 매기기

받은 리스트, 준 리스트 만들기
give[a][b] = 3 -> a가 b에게 3개를 줬다.
receive[b][a] = 1 -> b가 a에게 1개를 받았다.

---
정답 맞긴 했는데 굳이 배열 두개 안쓰고 give하나만으로도 해결 가능. 
+ 딕셔너리 enumerate로 한방에 처리, 변수 최적화

'''
def solution(friends, gifts):
    length = len(friends)
    give = [[0]*length for _ in range(length)]
    giftscore = [0] * length
    anslist = [0] * length
    
    dict = {name : idx for idx, name in enumerate(friends)}    
    
    for i in gifts:
        aname, bname = i.split()
        aind, bind = dict[aname], dict[bname]
        give[aind][bind] += 1
    
    for i in range(length):
        given = sum(give[i])
        received = sum(give[j][i] for j in range(length))
        giftscore[i] = given - received
        
    for i in range(length-1):
        for j in range(i+1, length):
            if give[i][j] > give[j][i]: # i가 j한테 준게 더 많으면
                anslist[i] += 1
            elif give[i][j] < give[j][i]: # 반대라면
                anslist[j] += 1
            else: # 같다면
                if giftscore[i] > giftscore[j]:
                    anslist[i] += 1
                elif giftscore[i] < giftscore[j]:
                    anslist[j] += 1
    return max(anslist)
                
        