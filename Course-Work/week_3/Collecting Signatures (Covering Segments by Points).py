>>
n = int(input())
l,coordinates = [],[]

for _ in range(n):
    a, b = [int(i) for i in input().split()]
    l.append((a,b))

l.sort(key = lambda x: x[1])

index = 0

while index < n:
    curr = lst[index]
    while index < n-1 and curr[1]>=lst[index+1][0]:
        index += 1
    coordinates.append(curr[1])
    index += 1
    
print(len(coordinates))
print(' '.join([str(i) for i in coordinates]))



@ CODED BY TSG405, 2021
