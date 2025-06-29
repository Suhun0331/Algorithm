n, m = map(int, input().split())

lst1 = []
lst2 = []
for _ in range(n):
    lst1.append(input().strip())
for _ in range(m):
    lst2.append(input().strip())

lst1.sort()
lst2.sort()

answer = []
idx = 0
for i in lst1:
    if idx >= m:
        break
    if i == lst2[idx]:
        answer.append(i)
        idx += 1
    else:
        while idx < m:
            if i > lst2[idx]:
                idx += 1
            elif i == lst2[idx]:
                answer.append(i)
                idx += 1
                break
            else:
                break

print(len(answer))
for i in answer:
    print(i)
