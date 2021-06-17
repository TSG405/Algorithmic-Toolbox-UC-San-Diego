>>
a=list(map(int,input().split()))
b=list(map(int,input().split()))

high = a[0]-1
low = 0

a.remove(a[0])
b.remove(b[0])

a.sort()

def bi(a,low,high,key):
    if (high < low):
        return (-1)
    mid = (high + low)//2
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return bi (a,low,mid-1,key)
    else:
        return bi (a,mid+1,high,key)

for tt in b:
    print( bi (a,low,high,tt), end = ' ')

    
    
@ CODED BY TSG405, 2021
