import bisect

def find (input, number, how_num):
    k = how_num

    insert_index = bisect.bisect_left(input, number)

    i, j = insert_index - 1, insert_index
    
    while k > 0 and i >= 0 and j < len(input):
        if abs(input[i] - number) <= abs(input[j] - number) or abs(abs(input[i]-number)-abs(input[j]-number)) < 0.0000001:
            i = i - 1
        else:
            j = j + 1
        k = k - 1

    if j >= len(input):
        while k > 0:
            i = i - 1
            k = k - 1
    i = i + 1
    return input[i:i+how_num]

find([1,2,3,4,4,7], 5.2, 2) #[4,4]
find([1,2,5,8,8,9,9], 10, 2)#[9,9]
find([1,2,2,4,5,6,9], 0, 3) #[1,2,2]
find([1,2,3,4,4,7], 6.5, 3) #[4,4,7]
find([1,2,3,4,4,6,6], 5, 3) #[4,4,6]
find([1,2,3,4,4,5,6], 4, 5) #[2,3,4,4,5]"""
