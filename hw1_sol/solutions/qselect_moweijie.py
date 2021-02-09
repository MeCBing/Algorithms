import random

def qselect(i, a):
    if a == []:
        return []
    idx=random.randint(0,len(a)-1)
    pivot = a[idx]

    a[0],a[idx]=a[idx],a[0]

    left = [x for x in a if x < pivot]
    if len(left) == i-1:
        return pivot
    if len(left) < i - 1:
        right = [x for x in a[1:] if x >= pivot]
        return qselect(i-len(left)-1,right)
    else:
        # a = left
        return qselect(i,left)

print (qselect(4,[4, 6, 19, 8, 10]))
