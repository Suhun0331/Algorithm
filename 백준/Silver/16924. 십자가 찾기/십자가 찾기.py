n,m=map(int,input().split())
  
array=[[0]*m for _ in range(n)]
for i in range(n):
  array[i]=list(input())

for i in range(n):
  for j in range(m):
    if array[i][j]=='.':
      array[i][j]=0
    elif array[i][j]=='*':
      array[i][j]=1

if n==0 or n==1 or n==2:
  print(-1)

else:
  pos=[]
  
  center=[]
  for i in range(n):
    for j in range(m):
      if array[i][j]==1:
        center.append([i,j])
        
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]

  for i,j in center:
    size=0
    flag=0
    x,y=i,j

    while(True):
      if(flag==1):
        break
      size+=1
    
      for dir in range(4):
        nx=x+dx[dir]*size
        ny=y+dy[dir]*size
        if nx<0 or nx>=n or ny<0 or ny>=m:
          flag=1
          break
        elif array[nx][ny]==0:
          flag=1
          break
        elif dir==3:
          array[x][y]+=1
          array[x+size][y]+=1
          array[x-size][y]+=1
          array[x][y+size]+=1
          array[x][y-size]+=1
          pos.append([i+1,j+1,size])

  flag2=1
  for i,j in center:
    if array[i][j]==1:
      print(-1)
      flag2=0
      break
  if(flag2):
    print(len(pos))
    for i in pos:
      for j in i:
        if j==i[2]:
          print(j)
        else:
          print(j,end=" ")