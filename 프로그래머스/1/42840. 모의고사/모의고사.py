def solution(answers):

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    index = 0
    one_c , two_c, three_c = 0, 0, 0
    for i in answers:
        if i == one[index%5]:
            one_c += 1
        if i == two[index%8]:
            two_c += 1
        if i == three[index%10]:
            three_c += 1
        index += 1
    check = max(one_c, two_c, three_c)
    answer = []
    if one_c == check:
        answer.append(1)
    if two_c == check:
        answer.append(2)
    if three_c == check:
        answer.append(3)
    return answer
    
    
