'''
아예 모르겠어서 인터넷 찾아봤음
ㅠ ㅅ ㅠ 
이분탐색 。。 몇 개 더 풀어봐야 할 듯
'''

def solution(n, times):
    left, right = min(times), max(times)*n
    while left<=right:
        mid = (left + right)//2
        posible = 0
        for i in times:
            posible += (mid//i)
        if posible >= n:
            right = mid-1 
        elif posible < n:
            left = mid+1
            
    return left



