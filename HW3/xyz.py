def find(input):
    #input.sort()
    newinput = sorted(input)

    ans = []
    
    for k, n in enumerate(input):
        i, j = 0, len(input) - 1#k-1

        while i < j:
            if newinput[i] + newinput[j] == n:
                ans.append((newinput[i], newinput[j], input[k]))
                i = i + 1
            else:
                j = j - 1
    return ans

#find([1, 4, 2, 3, 5]) #[(1,3,4), (1,2,3), (1,4,5), (2,3,5)]