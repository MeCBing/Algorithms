import random

def merge(leftinput, rightinput):
    finish = []
    i, j = 0, 0
    while len(finish) != (len(leftinput) + len(rightinput)):
        smallone = min(leftinput[i], rightinput[j])
        if smallone == leftinput[i]:
            i = i + 1
        else:
            j = j + 1
        finish.append(smallone)
        if i == len(leftinput):
            finish = finish + rightinput[j:]
        elif j == len(rightinput):
            finish = finish + leftinput[i:]

    return finish

def mergesort(input):
    if len(input) == 1:
        return input
    else:
        mid = int(len(input)/2)
        return merge(mergesort(input[:mid]), mergesort(input[mid:]))

mergesort([4, 2, 5, 1, 6, 3])
mergesort([4, 2, 5, 1, 6, 3, 8])
mergesort(random.sample(range(10),10))