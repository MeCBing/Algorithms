import random

def findpath(input):
    if input[0] == []:
        leftbig = [0, 0]
    else:
        leftbig = findpath(input[0])
    if input[2] == []:
        rightbig = [0, 0]
    else:
        rightbig = findpath(input[2])   
    if leftbig[1] == 1:
        leftbig[0] = leftbig[0] + 1
    if rightbig[1] == 1:
        rightbig[0] = rightbig[0] + 1       
    newbig = leftbig[1] + rightbig[1]
    return [max(leftbig[0],newbig,rightbig[0]), max(leftbig[1],rightbig[1]) + 1] 
        

def longest(input):
    if input == []:
        return 0
    else:
        ans = findpath(input)
        return ans[0]



#longest([[], 1, []])
#longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]) 
#random.sample(range(200),200)
#longest(sort(random.sample(range(200),200))) == 25