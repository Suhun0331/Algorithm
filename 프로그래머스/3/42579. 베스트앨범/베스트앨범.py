'''
딕셔너리 만들어서 key에 장르 저장하고 value에는 (plays, 인덱스) 저장
sum(value[0])으로 장르 순서 먼저 결정
value에 저장돼있는 plays 기준으로 정렬하고, 앞에서 두개씩 인덱스 뽑아서 answer에 추가
'''
from collections import defaultdict

def solution(genres, plays):
    dict = defaultdict(list)
    answer = []
    
    for i in range(len(genres)):
        dict[genres[i]].append([plays[i], i])
        
    dict = sorted(dict.values(), key = lambda x : sum(i for i, _ in x), reverse = True)
    # print(dict)
    
    for i in dict:
        # print(i)
        i.sort(key = lambda x : x[0], reverse = True)
        for j in range(len(i)):
            if j >= 2:
                break
            answer.append(i[j][1])
    
    return answer