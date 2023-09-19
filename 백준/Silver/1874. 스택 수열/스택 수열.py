num = int(input())
stack_1 = []
stack_2 = []

for i in range(num):
    stack_2.append(int(input()))

count= 0
check = 0
add = 1
answer = []
while True:
    stack_1.append(add)
    answer.append("+")
    add += 1
    count += 1
    while stack_1[count-1] == stack_2[check]:
        stack_1.pop()
        check += 1
        count -= 1
        answer.append("-")
        if len(stack_1) == 0:
            break
    if len(stack_1) == 0 and check == num:
        for i in answer:
            print(i)
        break
    if add == num+1 and stack_1[count-1] != stack_2[check]:
        print("NO")
        break