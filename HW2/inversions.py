def swap(leftinput, rightinput):
    i, j, count = 0, 0, 0
    while i < len(leftinput):
        smallone = min(leftinput[i], rightinput[j])
        if smallone == leftinput[i]:
            i = i + 1
        else:
            leftinput[i], rightinput[j] = rightinput[j], leftinput[i] 
            count = count + 1
            i = i + 1
            while j < len(rightinput)-1 and rightinput[j] > rightinput[j+1] and len(rightinput) > 1:
                rightinput[j], rightinput[j+1] = rightinput[j+1], rightinput[j]
                count = count + 1
                j = j + 1
            j = 0            

    return count, leftinput + rightinput

def count(input):
    if len(input) == 1:
        return 0, input
    else:
        mid = int(len(input)/2)
        leftcount, leftlist = count(input[:mid])
        rightcount, rightlist = count(input[mid:])
        swapcount, swaplist = swap(leftlist, rightlist)
        return leftcount + rightcount + swapcount, swaplist

def num_inversions(input):
    getcount, getlist = count(input)
    print(getlist)
    return getcount

num_inversions([4, 1, 3, 2])
num_inversions([2, 4, 1, 3])
num_inversions([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])