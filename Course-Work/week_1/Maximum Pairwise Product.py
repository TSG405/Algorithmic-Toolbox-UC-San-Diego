>>
def max_pairwise_product(n, a):
    if n>1:
        a.sort(reverse=True)
        return (a[0]*a[1])
    else:
        return -1

n = int(input())
a = [int(x) for x in input().split()]
print(max_pairwise_product(n, a))



@ CODED BY TSG405, 2021
