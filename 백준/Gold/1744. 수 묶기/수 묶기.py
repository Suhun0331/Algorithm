n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

if n != 1:
    num.sort(reverse = True)

    answer = 0

    for i in range(0, len(num), 2):
        if i + 1 < len(num):
            if num[i] > 0 and num[i+1] > 0:
                #print(max(num[i]*num[i+1], num[i] + num[i+1]))
                answer += max(num[i]*num[i+1], num[i] + num[i+1])
            elif num[i] > 0:
                answer += num[i]
                break
            else:
                break
        else:
            if num[i] > 0:
                answer += num[i]
    #print(answer)
        
    num.sort()

    for i in range(0, len(num), 2):
        if i + 1 < len(num):
            if num[i] < 0 and num[i+1] <= 0:
                answer += num[i]*num[i+1]
            elif num[i] < 0:
                answer += num[i]
                break
            else:
                break
        else:
            if num[i] < 0:
                answer += num[i]
        #print(answer)


    print(answer)
else:
    print(num[0])
