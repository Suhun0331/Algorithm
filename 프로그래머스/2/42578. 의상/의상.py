from itertools import combinations

def solution(clothes):
    answer = 1
    
    dict = {}
    for i in clothes:
        if i[1] in dict:
            dict[i[1]] += 1
        else:
            dict[i[1]] = 1
        
    for val_cnt in dict.values():
        answer *= val_cnt + 1
    return answer - 1