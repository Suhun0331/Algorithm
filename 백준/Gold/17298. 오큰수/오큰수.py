import sys

num = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

answer = [-1]*num
stack = []

for i in range(num):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)

        
for i in answer:
    print(i, end = ' ')