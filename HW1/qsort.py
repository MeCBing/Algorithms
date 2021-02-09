
def sort(input):
    if input == []:
        return []
    else:
        pivot = input[0]
        left = [n for n in input if n < pivot]
        right = [n for n in input[1:] if n >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def sorted(input):
    if input == []:
        return []
    else:
        pivot = input[1]
        left = input[0]
        right = input[2]
        return sorted(left) + [pivot] + sorted(right)

def insertsorted(input, number):
    if input == []:
        return input
    else:
        pivot = input[1]
        left = input[0]
        right = input[2]
        if number < pivot:
            return insertsorted(left, number)
        if number > pivot:
            return insertsorted(right, number)
        return [input]

def _search(input, number):
    if input == []:
        return input
    else:
        pivot = input[1]
        left = input[0]
        right = input[2]
        if number < pivot:
            return _search(left, number)
        if number > pivot:
            return _search(right, number)
        #print(input)
        return input
        
def search(input, insertnumber):
    x = _search(input, insertnumber)
    if x != []:
        return True
    else:
        return False
def insert(input, insertnumber):
    x = _search(input, insertnumber)
    if x == []:
        x += [[]] + [insertnumber] + [[]]

#tree = sort([4,2,6,3,5,7,1,9])

#sorted(tree)
#search(tree, 100)
#search(tree, 1)
#insert(tree, 6.5)
#insert(tree, 10) 
#_search(tree, 3)
#_search(tree, 0)
#tree
#_search(tree, 0) is _search(tree, 20)
#_search(tree, 0) == _search(tree, 20)