>>
def GCD(a, b): 
    while(b):
        a,b = b,a % b     
    return (a)

a,b = map(int,input().split())
if (a > b): gcd = GCD(a, b)
else: gcd = GCD(b, a)

LCM = (a*b)//(gcd)
print(LCM)



@ CODED BY TSG405, 2021
