import sys
 
num = int(input())
 
k = list(map(int,sys.stdin.readline().strip().split(" ")))
 
 
temp = [ ]
 
for i in range(0,len(k)):
 
 
 
    for j in range(0,len(temp)):
 
        if k[i]+temp[j]>0:
            temp.append(k[i]+temp[j])
 
        if k[i]-temp[j]>0:
            temp.append(k[i]-temp[j])
 
        if -k[i]+temp[j]>0:
            temp.append(-k[i]+temp[j])
    temp.append(k[i]) 
 
temp = list(set(temp))
 
 
 
 
print(sum(k)-len(temp))