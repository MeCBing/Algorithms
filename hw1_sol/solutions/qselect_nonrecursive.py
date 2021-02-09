from random import *

def qselect(k, a):
    if k < 1 or k > len(a) or a == []:
        return []
    while a != []:
        r_index = randint(0, len(a)-1)
        a[0], a[r_index] = a[r_index], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        l_left = len(left)
        if k-1 < l_left:
            #return qselect(k, left)
            a = left
        elif k-1 == l_left:
            return pivot
        else:
            right = [x for x in a[1:] if x >= pivot]
            #return qselect(k-l_left-1, right)
            k, a = k-l_left-1, right

print(qselect(4, [5,1,6,2,8,3,7,9]))
