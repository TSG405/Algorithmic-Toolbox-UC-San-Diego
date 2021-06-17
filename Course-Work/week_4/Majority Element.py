>>
n=int(input())
l=list(map(int,input().split()))

l.sort()

def freq(l,k):
    d={}
    c=0
    for item in reversed(l):
        d[item] = d.get(item,0) + 1
        if d[item] >= c:
            c = d[item]
        if (c > k//2):
            return 1
            break
    return (0)

print(freq(l,n))



@ CODED BY TSG405, 2021
