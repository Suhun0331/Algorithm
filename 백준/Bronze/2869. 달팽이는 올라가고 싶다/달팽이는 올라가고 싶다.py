a, b, v = map(int, input().split())

day = int((v-a)/(a-b))

if (v-a)%(a-b) == 0:
    print(day+1)
else:
    print(day+2)