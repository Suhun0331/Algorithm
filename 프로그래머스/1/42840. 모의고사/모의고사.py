def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    onescore, twoscore, threescore = 0, 0, 0
    for i in range(len(answers)): # 5
        if answers[i] == one[i%len(one)]:
            onescore += 1
        if answers[i] == two[i%len(two)]:
            twoscore += 1
        if answers[i] == three[i%len(three)]:
            threescore += 1
    
    maxnum = max(onescore, twoscore, threescore)
    if maxnum == onescore:
        answer.append(1)
    if maxnum == twoscore:
        answer.append(2)
    if maxnum == threescore:
        answer.append(3)
    return answer
        