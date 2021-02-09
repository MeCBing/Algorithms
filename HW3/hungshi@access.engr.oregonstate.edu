import random
def qselect(input, number):
    pivot = random.randrange(len(input))

    left = [n for n in input if n < input[pivot]]

    if (len(left) + 1) == number:
        return input[pivot]
    elif len(left) < number:
        input[0],input[pivot] = input[pivot], input[0]
        right = [n for n in input[1:] if n >= input[0]]
        input[0],input[pivot] = input[pivot], input[0]
        return qselect(right, number-len(left)-1)
    elif len(left) >= number:
        return qselect(left, number)

def find(input, number, wantnumber):
    check = [-1 for n in input]

    gap = [abs(n-number) for n in input]

    qselectans = qselect(gap, wantnumber)

    for i, j in enumerate(gap):
        if j + 0.0000001 < qselectans: 
            check[i] = 0 
            wantnumber -= 1

    for i, j in enumerate(gap):
        if wantnumber == 0:
            break
        if abs(j-qselectans) < 0.0000001:
            check[i] = 0
            wantnumber -= 1

    return [input[x] for x in range(len(check)) if check[x] == 0]

find([4,1,3,2,7,4], 5.2, 2)
find([4,1,3,2,7,4], 6.5, 3)
find([5,3,4,1,6,3], 3.5, 2)