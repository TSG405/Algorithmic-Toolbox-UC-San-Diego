>>
def fibo(n):
    a,b = 0, 1
    for _ in range(2,n+1):
        c = a+b
        c = c%10
        b,a = c,b
    if (c!=0): print(c-1)
    else: print(9)

n = int(input())

if (n<=1): print(n)  
else:
    q = (n+2)%60
    if q==1:
        print(0)
    elif q==0:
        print(9)
    else:
        fibo(q)

        
        
@ CODED BY TSG405, 2021
