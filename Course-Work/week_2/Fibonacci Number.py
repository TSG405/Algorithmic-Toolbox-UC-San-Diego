>>
def fibo(n):
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        b, a = c, b
    print(c)

n = int(input())
if n>1:
    fibo(n)
else:
    print(n)



@ CODED BY TSG405, 2021
