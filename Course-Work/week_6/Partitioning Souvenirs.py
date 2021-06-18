>>
def sou(arr,n):
    s=i=j=0
    for i in range(n): s+=arr[i]
    if s%3!=0: return False
    part=[[True for i in range(n+1)]for j in range (s//3+1)]
    
    for i in range(0,n+1): part[0][j]=True
    for i in range(1,s//3+1): part[i][0]=False
    for i in range(1,s//3+1):
        for j in range(1,n+1):
            part[i][j]=part[i][j-1]
            if i >=arr[j-1]:
                part[i][j]=(part[i][j] or part[i-arr[j-1]][j-1])
                
    return(part[s//3][n])

n=int(input())
arr=list(map(int,input().split()))

Z=sou(arr,n)
if (Z==True): print(1)
else: print(0)
  
  
  
@ CODED BY TSG405, 2021
