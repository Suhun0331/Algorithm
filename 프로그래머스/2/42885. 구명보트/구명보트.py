'''
1 1 3 8 9 -> 3
사람들 무거운 순으로 정렬
해당 사람 + 제일 가벼운 사람 이 보트보다 가벼우면 + 1, 제일 가벼운 사람 제거
그게 아니면 그냥 + 1
'''

def solution(people, limit):
    answer = 0
    
    people.sort(reverse = True)
    first = 0
    last = len(people)-1
    team = 0
    
    while first < last:
        if people[first] + people[last] <= limit:
            last -= 1
            team += 1
        first += 1
    
    return len(people) - team