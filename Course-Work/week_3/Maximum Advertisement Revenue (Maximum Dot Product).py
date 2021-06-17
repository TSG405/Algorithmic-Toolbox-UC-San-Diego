>>
n=int(input())
l3=[]

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

l1.sort()
l2.sort()

for t in range(0,n): l3.append(l1[t]*l2[t])
print(sum(l3))  



@ CODED BY TSG405, 2021
