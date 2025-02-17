'''
1 1 3 8 9 -> 3
사람들 무거운 순으로 정렬
해당 사람 + 제일 가벼운 사람 이 보트보다 가벼우면 + 1, 제일 가벼운 사람 제거
그게 아니면 그냥 + 1
'''

def solution(people, limit):
    answer = 0
    
    people.sort(reverse = True)
    arr = [False] * (len(people))
    last = len(people)-1
    for i in range(len(people)):
        #print(arr)
        if arr[i]:
            #print('check')
            return answer
        if people[i] + people[last] <= limit:
            arr[i], arr[last] = True,True
            last -= 1
        else:
            arr[i] = True
        answer += 1
    
    return answer