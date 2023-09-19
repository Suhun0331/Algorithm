n = int(input())
endnumber=666
count = 0

while True:
    if '666' in str(endnumber):
        count += 1
    if count == n:
        break
    endnumber += 1
print(endnumber)