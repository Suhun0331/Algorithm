'''
1 1 3 8 9 -> 3
사람들 무거운 순으로 정렬
해당 사람 + 제일 가벼운 사람 이 보트보다 가벼우면 + 1, 제일 가벼운 사람 제거
그게 아니면 그냥 + 1
'''

def solution(people, limit):
    people.sort()
    first = 0
    last = len(people)-1
    team = 0
    
    while first < last:
        if people[first] + people[last] <= limit:
            first += 1
            team += 1
        last -= 1
    
    return len(people) - team