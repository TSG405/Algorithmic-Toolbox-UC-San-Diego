>>
def fibo(n):
    a, b = 0, 1
    for _ in range(2, n+1):
        c = a+b
        c = c%10
        b, a = c, b
    return c
  
n = int(input())
q,qq = n%60,(n+1)%60 

if q<2: a = q
else: a = fibo(q)
  
if qq<2: b = qq
else: b = fibo(qq)
  
print((a*b)%10)



@ CODED BY TSG405, 2021
