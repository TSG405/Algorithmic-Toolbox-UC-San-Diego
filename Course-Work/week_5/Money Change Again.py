>>
import math

money = int(input())
denominations = [1, 3, 4]
minCoins = [0] + [math.inf]*money

for i in range(1, money+1):
    for j in denominations:
        if i>=j:
            coins = minCoins[i-j]+1
            if coins < minCoins[i]:
                minCoins[i] = coins

print(minCoins[money])


'''
         ---OR---

n=int(input())
f=[0 for tsg in range(n+1)]
f[0],f[1],i=0,1,2

def ch3(i):
    if (i>=4):
        z3 = i-4
        return z3
    else: return -1

def ch2(i):
    if (i>=3):
        z2 = i-3
        return z2
    else: return -1

while(i<=n):
    z3=z2=z1=2*n
    
    k3=ch3(i)
    if (k3!=-1): z3=f[k3]
    else: z3=n*2
      
    k2=ch2(i)
    if (k2!=-1): z2=f[k2]
    else: z2=n*2
      
    k1=i-1
    z1=f[k1]
    j=min(z3,z2,z1)
    
    if (j==z3): f[i]=z3+1
    elif (j==z2): f[i]=z2+1
    else: f[i]=z1+1
      
    i+=1

if(n==1): print(1)
else: print(f[-1])
'''


@ CODED BY TSG405, 2021
