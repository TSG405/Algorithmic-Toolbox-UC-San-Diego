>>
def fibo(n):
    a,b = 0, 1
    for i in range(2,n+1):
        c = a+b
        c = c%10
        b, a = c, b
    return (c-1)

m,n = [int(i) for i in input().split()]

if n<2: print(n)  
else:
    q = (n+2)%60
    qq = (m+1)%60
    
    if q<=1: a = q-1
    else: a = fibo(q)
      
    if qq<=1: b = qq-1
    else: b = fibo(qq)

    if a>=b: print(a-b)
    else: print(10+a-b)

      
      
@ CODED BY TSG405, 2021
