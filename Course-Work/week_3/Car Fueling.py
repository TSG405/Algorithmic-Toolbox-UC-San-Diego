>>
t=int(input())
g=int(input())
n=int(input())

f=[]
flag,i=0,0

e=list(map(float,input().split()))
e.append(t)

while(i<t):
    p=i
    i+=g
    if (i in e): f.append(i)
    else:
        for z in range(0,g):
            if (i in e):
                f.append(i)
                break
            else: i-=1
        if(p==i):
            flag=1
            break
            
if (flag==0): print(len(f)-1)
else: print(-1)



@ CODED BY TSG405, 2021
