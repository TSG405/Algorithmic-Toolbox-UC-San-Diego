>>
import collections

i=list(map(int,input().split()))
n,w,c=i[0],i[1],1
v1,w1=[],[]

for i3 in range (0,n):
    i4=input().split()
    for i5 in i4:
        if (c%2 == 0):
            w1.append(int(i5))
        else:
            v1.append(int(i5))
        c+=1
        
a=dict()
aa=dict()

for j in range (0,n):
    a[float(v1[j]/w1[j])] = w1[j]
oa = collections.OrderedDict(sorted(a.items(),reverse=True))
oa[0]=0

def knapsack (oa,w,n,su):
    for r in oa:
        if w==0 or r==0:
            return(su)
        else:
            z=oa[r]
            comp=min(z,w)
            su+=comp*r
            z-=comp
            w-=comp
            
print("{:.4f}".format(knapsack(oa,w,n,0)))



@ CODED BY TSG405, 2021
