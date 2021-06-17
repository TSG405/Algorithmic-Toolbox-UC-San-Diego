>>
n=int(input())

f=[[] for tsg in range(n+1)]
f[0],f[1],i = 0,[0,1],2

def ch3(i):
    if (i%3 == 0):
        z3 = i//3
        return z3
    else: return -1

def ch2(i):
    if (i%2 == 0):
        z2 = i//2
        return z2
    else: return -1

while(i<=n):
    z3=z2=z1=2*n
    
    k3=ch3(i)
    if (k3!=-1):
        z31=f[k3]
        z3=z31[0] + 1
    else: z3=n*2
        
    k2=ch2(i)
    if (k2!=-1):
        z21=f[k2]
        z2=z21[0] + 1
    else: z2=n*2
        
    k1=i-1
    z11=f[k1]
    z1=z11[0]+1
    
    j=min(z3,z2,z1)
    f[i].append(j)
    if (j==z3): f[i].append(k3)
    elif (j==z2): f[i].append(k2)
    else: f[i].append(k1)
    i+=1

fb=[]

if(n==1):
    print(0)
    print(1)
else:
    while(n>=2):
        q=f[n]
        qq=q[-1]  
        fb.append(n)
        n=qq
        
    fb.append(1)
    fb.sort()
    print(len(fb)-1)
    for tsg in fb:
        print(tsg,end =" ")


        
@ CODED BY TSG405, 2021
