>>
l = []
s, p = [int(i) for i in input().split()]
points = input().split()
segment_count = 0
point_segment_map = {}
temp = ''

for i in range(s):
    a, b = [int(i) for i in input().split()]
    l.append((a,'l'))
    l.append((b,'r'))

for i in points:
    l.append((int(i),'p'))

l.sort()

for i in master_list:
    if i[1] == 'l': segment_count += 1
    elif i[1] == 'r': segment_count -= 1
    else: point_segment_map[i[0]] = segment_count

for i in points:
    temp += str(point_segment_map[int(i)]) + ' '
print(temp[:-1])



@ CODED BY TSG405, 2021
