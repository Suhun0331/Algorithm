'''
유니온-파인드 (인터넷 찾아봄)
간선 간 서로소 or 이어져있는지 확인하는 문제는
유니온 파인드 먼저 생각하기

처음 입력 받은 거 간선 추가

다음 입력 받으면 그 두개 부모 노드 찾아서 똑같으면
사이클 만들어진거니까 count 리턴

그게 아니면 간선 추가, 부모 테이블 업데이트
'''
import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())

parent = [i for i in range(n)]
count = 0
check = False
for i in range(m):
    count += 1
    x, y = map(int, input().split())
    if find(x) == find(y):
        check = True
        break
    else:
        union(x, y)
if not check:
    print(0)
else:
    print(count)
