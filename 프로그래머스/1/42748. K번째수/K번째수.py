def solution(array, commands):
    answer = []
    sub = []
    for i in commands:
        sub = array.copy()
        sub = sub[i[0]-1 : i[1]]
        sub.sort()
        #print(sub)
        answer.append(sub[i[2]-1])
        
    return answer