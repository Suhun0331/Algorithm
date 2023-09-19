a = int(input())
b = int(input())

step1 = a * (b%10)
step2 = a * ((b%100)//10)
step3 = a * (b//100)
step4 = a*b

print(step1)
print(step2)
print(step3)
print(step4)