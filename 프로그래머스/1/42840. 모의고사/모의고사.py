def solution(answers):

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    index = 0
    score = [0, 0, 0]
    for i in answers:
        if i == one[index%5]:
            score[0] += 1
        if i == two[index%8]:
            score[1] += 1
        if i == three[index%10]:
            score[2] += 1
        index += 1
    check = max(score)
    answer = []
    if score[0] == check:
        answer.append(1)
    if score[1] == check:
        answer.append(2)
    if score[2] == check:
        answer.append(3)
    return answer
    
    
