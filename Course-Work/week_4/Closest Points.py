>>
import math
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x) 
    mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array

    # Create a subarray of points not further than delta from midpoint on x-sorted array
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]

    best = delt
    ln_y = len(s_y) 
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 5, ln_y)):    # Check only 5 points
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best

def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:  
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi

def closest_pair(ax, ay):
    ln_ax = len(ax) 
    if ln_ax <= 3:
        return brute(ax)  # bruteforce comparison
    mid = ln_ax // 2  
    Qx = ax[:mid]  # split 1
    Rx = ax[mid:]  # split 2

    midpoint = ax[mid][0]
    Qy = list()
    Ry = list()
    for x in ay:  
        if x[0] < midpoint:
           Qy.append(x)
        else:
           Ry.append(x)
  
    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)

    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    if d <= mi3: return mn[0], mn[1], d
    else: return p3, q3, mi3

def solution(a):
    ax = sorted(a, key=lambda x: x[0])  # Presorting x-wise O(nlogn)
    ay = sorted(a, key=lambda x: (x[1], x[0]))  # Presorting y-wise then x-wise O(nlogn)
    p1, p2, mi = closest_pair(ax, ay)  
    return mi


p = list()
n = int(input())
for i in range(n):
    p.append([int(i) for i in input().split()])

print(solution(p))



@ CODED BY TSG405, 2021
