num = int(input())

line = 0
end = 0
while num>end:
    line += 1
    end += line
#line - 몇 번째 묶음인지
diff = end - num#한 묶음에서 몇 번째인지(뒤에서)

if line%2 == 0:
    top = line - diff
    bottom = diff+1
else:
    top = diff+1
    bottom = line - diff

print("%d/%d"%(top,bottom))