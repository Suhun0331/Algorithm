import sys

inx = 1
while True:
    word = list(map(str, sys.stdin.readline().strip()))

    if word.count("-") >= 1:
        break

    cnt = 0
    stack = [word[0]]
    for i in range(1, len(word)):

        if stack:
            if stack[-1] == '{' and word[i] == '}':
                stack.pop()
                continue

        stack.append(word[i])

    for j in range(0, len(stack), 2):
        if stack[j] == "}":
            cnt += 1

        if stack[j + 1] == "{":
            cnt += 1

    print("{0}. {1}".format(inx, cnt))
    inx += 1
                