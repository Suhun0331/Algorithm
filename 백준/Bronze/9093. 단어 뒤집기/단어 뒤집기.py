num = int(input())

for _ in range(num):
    sen = list(input().split())
    for i in range(len(sen)):
        #sen[i].reverse()
        sen[i] = sen[i][::-1]
    for i in sen:
        print(i, end = ' ')
    print()