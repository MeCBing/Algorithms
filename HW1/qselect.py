import random
# make the function to do the sort and find the order.
def sort(index, input, k):
    #put the random index in list to pivot.
    r = 0
    if(input.__len__() != 0):
        r = random.randrange(0,input.__len__())
    #print("r : ",r)
    pivot = input[r]
    #print("pivot", pivot)
    # a list put the input data which is small than pivot.
    left = [n for n in input if n < pivot ]
    # x = left list length in input; k = how many length in last list length
    x = left.__len__() + k
    
    # (index == x + 1) means the order which is pivot.
    if index == x + 1:
        # return the answer.
        return pivot
    # (index <= x) means the order which is in the left list.
    elif index <= x:
        # order in the left list, so keep finding; also not sure the left.
        return sort(index, left, k)
    # else means the order which is in the right list.
    else:
        # swap input[0] and input[r]
        # a list put the input data which is bigger than pivot or sam.
        #input[0],input[r] = input[r],input[0]
        #right = [n for n in input[1:] if n >= pivot]
        input.pop(r)
        right = [n for n in input if n >= pivot]
        #print(right)
        # order in the right list, so keep finding.
        return sort(index, right, x + 1)

# make the function call qselect, and input is the list which you input; also index is the order which you want.
def qselect(index, input):
    # just make sure the input is ok.
    #return sort(index, input, 0)
    if input != [] and index > 0 and index <= input.__len__():
        # call function sort.
        return sort(index, input, 0)
    else:
        # incorrect return.
        return
#qselect(2,[1,2,7,3,1,1,1,11,2,8,3])
#qselect(2, [3, 10, 4, 7, 19])
#qselect(4, [11, 2, 8, 3])
#qselect(5, [1,2,3,4,5])