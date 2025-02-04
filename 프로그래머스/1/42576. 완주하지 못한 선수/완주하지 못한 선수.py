def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p  # 차이가 나는 순간 반환
    
    return participant[-1]  # 마지막 남은 선수 반환