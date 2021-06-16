>>
def lastdigit(n):
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        c = c % 10
        b, a = c, b
    print(c)
    
n = int(input())
if n<=1:
    print(n)
else:
    lastdigit(n)

    
    
@ CODED BY TSG405, 2021
