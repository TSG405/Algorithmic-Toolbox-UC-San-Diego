>>
def GCD(a, b): 
    while(b):
        a,b = b,a % b     
    return (a)

x,y = map(int,input().split())
print(GCD(x,y)) 



@ CODED BY TSG405, 2021
