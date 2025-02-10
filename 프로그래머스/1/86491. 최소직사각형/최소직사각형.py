def solution(sizes):
    answer = 0
    maxx = []
    minn = []
    for i in sizes:
        maxx.append(max(i))
        minn.append(min(i))
                
    return max(maxx)*max(minn)
