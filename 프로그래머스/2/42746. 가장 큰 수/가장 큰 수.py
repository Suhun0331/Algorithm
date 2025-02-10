

def solution(numbers):
    answer = ''
    arr = []
    for i in numbers:
        arr.append(str(i))
    arr.sort(reverse = True, key = lambda x : x*3)
    for i in arr:
        answer += i
    return str(int(answer))