'''
각 층의 길이는 층의 수와 동일
쭉 내려가서 제일 아랫층의 max값 찾기
각 층의 값은 전 층의 max값 + 현재 값 (두개의 값이 올 수 있으니 max()로 값 넣기)
맨 앞과 맨 뒤는 값 하나밖에 못 옴.
'''
def solution(triangle):
    lst = [[0]*(i+1) for i in range(len(triangle))]
    lst[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                lst[i][j] = lst[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                lst[i][j] = lst[i-1][j-1] + triangle[i][j]
            else:
                lst[i][j] = max(lst[i-1][j-1], lst[i-1][j]) + triangle[i][j]
    answer = max(lst[-1])
    return answer