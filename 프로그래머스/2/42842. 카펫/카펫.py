'''
brown을 보고 나올 수 있는 n x m 을 구함.
해당 n x m일 때 필요한 yellow를 구한 후, 입력 받은 yellow랑 일치하는지 확인

ex) brown = 10 -> 3 x 4 -> yellow는 3x4 - brown(10) = 2
brown = 24 -> 3 x <(24 - 3 x 2)를 // 2 하고 + 2 한게 가로 길이> -> 3 x 11
3 x 11일 때 yellow는 3 x 11 - 24 = 9 -> x
4 x <(24-4x2)//2+2> 4 x 10 -> 40 - 24 = 16 -> x
5 x <(24-5x2)//2+2> 5 x 9 -> 45 - 24 = 21 -> x
6 x 8 -> 48 - 24 = 24

'''

def solution(brown, yellow):
    answer = []
    
    start = (brown-3*2)//2 + 2
    print(start)
    
    for i in range(3, brown):
        width = i*start-brown
        if yellow == width:
            return [max(i, start), min(i, start)]
        start -= 1
    
    return answer