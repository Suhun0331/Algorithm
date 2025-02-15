n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

ranks = []

for i in range(n):
    rank = 1
    for j in range(n):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

print(*ranks)
