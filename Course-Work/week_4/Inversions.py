>>
def merge(left, right):
    i, j, inversion_counter = 0, 0, 0
    final = []
    while i < len(left) and j< len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            inversion_counter += len(left) - i
            j += 1

    final += left[i:]
    final += right[j:]
    return final, inversion_counter

def mergesort(arr):
    global c
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sorted_arr, temp = merge(left, right)
    c += temp
    return sorted_arr

c = 0
n = int(input())
l = [int(i) for i in input().split()]
mergesort(l)
print(c)



@ CODED BY TSG405, 2021
