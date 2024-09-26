import sys
input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]


#array 전체 확인
#혹시 값이 다르면 9등분 한 크기로 함수 호출(재귀)
#값 모두 같으면 해당 값 + 1 하고 리턴

#시작 좌표 + 3, 배열 크기는 n/3 2n/3

answer = [0] * 5
def paper(x, y, n):
    check = array[x][y]
    #print(n)
    if n == 1:
        answer[check] += 1
        return
    for i in range(n):
        for j in range(n):
            if array[x + i][y + j] == check:
                continue
            else:
                paper(x, y, n//3)
                paper(x + n//3, y, n//3)
                paper(x, y + n//3, n//3)
                paper(x + n//3, y + n//3, n//3)
                paper(x + (n//3)*2, y, n//3)
                paper(x, y + (n//3)*2, n//3)
                paper(x + (n//3)*2, y + (n//3)*2, n//3)
                paper(x + (n//3)*2, y + n//3, n//3)
                paper(x + n//3, y + (n//3)*2, n//3)
                return
    answer[check] += 1

paper(0, 0, n)

print(answer[-1])
print(answer[0])
print(answer[1])
