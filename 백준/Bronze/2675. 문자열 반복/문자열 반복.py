a = int(input())

for i in range(a):
    num, sen = input().split()
    for i in sen:#문자열 자체를 for문에 사용 가능
        print(i*int(num), end="")
    print()#줄바꿈 하는 방법
    