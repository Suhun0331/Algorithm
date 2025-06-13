'''
낱개로 제일 싼 가격과 세트로 제일 싼 가격 구함
all 세트 vs all 낱개 vs 세트 + 낱개 중 min 구하기
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
min_set = 1001
min_one = 1001
for _ in range(m):
    a, b = map(int, input().split())
    min_set = min(min_set, a)
    min_one = min(min_one, b)

print(min(min_set*(n//6+1), min_one*n, min_set*(n//6)+min_one*(n%6)))