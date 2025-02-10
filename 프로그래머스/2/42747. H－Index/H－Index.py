'''
오름차순 정렬 -> 0 1 3 5 6
배열 내 현 위치 index 변수 생성하고, i가 배열[index]보다 크거나 같아지면 index + 1
for i in range(0, arr[마지막]) -> 전체 길이 - index가 i보다 크면 answer = i
'''

def solution(citations): #10 11 13 13 15 16
    answer = 0
    citations.sort()
    index = 0
    for i in range(citations[-1]): # 0 ~ 15
        
        if len(citations) - index >= i and index <= i:
            answer = i
        
        if citations[index] <= i:
            index += 1
        
    return answer