'''
각 층의 길이는 층의 수와 동일
쭉 내려가서 제일 아랫층의 max값 찾기
각 층의 값은 전 층의 max값 + 현재 값 (두개의 값이 올 수 있으니 max()로 값 넣기)
맨 앞과 맨 뒤는 값 하나밖에 못 옴.
'''
def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])